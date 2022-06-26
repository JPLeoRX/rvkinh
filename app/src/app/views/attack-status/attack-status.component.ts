import { Component, OnInit } from '@angular/core';
import {AttackOrchestration} from "../../message-protocol/attack-orchestration.model";
import {ClientService} from "../../services/client.service";
import {Worker} from "../../message-protocol/worker.model";

@Component({
  selector: 'app-attack-status',
  templateUrl: './attack-status.component.html',
  styleUrls: ['./attack-status.component.css']
})
export class AttackStatusComponent implements OnInit {
  loadingWorkers: boolean = false;
  hasResultWorkers: boolean = false;
  hasErrorWorkers: boolean = false;
  listOfWorkers: Worker[] = [];
  listOfClusters: string[] = [];

  loadingStatus: boolean = false;
  hasResultStatus: boolean = false;
  hasErrorStatus: boolean = false;
  attackOrchestrationStatus: AttackOrchestration = null!;

  constructor(private _clientService: ClientService) { }

  ngOnInit(): void {
    this.loadWorkers();
    this.loadStatus();

    setInterval(() => {
      this.reloadWorkers();
      this.reloadStatus();
    }, 3000)
  }

  loadWorkers() {
    console.log('attack-status.component.loadWorkers(): Started')
    this.hasResultWorkers = false;
    this.hasErrorWorkers = false;
    this.loadingWorkers = true;

    this._clientService.workersAlive().subscribe({
      next: (output: Worker[]) => {
        this.listOfWorkers = output;
        this.listOfClusters = Array.from(new Set(this.listOfWorkers.map(e => e.cluster_id)));
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

  loadStatus(): void {
    console.log('attack-status.component.loadStatus(): Started')
    this.hasResultStatus = false;
    this.hasErrorStatus = false;
    this.loadingStatus = true;

    this._clientService.attackOrchestrationStatus().subscribe({
      next: (output: AttackOrchestration) => {
        this.attackOrchestrationStatus = output;
        this.loadingStatus = false;
        this.hasErrorStatus = false;
        this.hasResultStatus = true;
      },
      error: (err) => {
        this.loadingStatus = false;
        this.hasResultStatus = false;
        this.hasErrorStatus = true;
      }
    });
  }

  reloadWorkers() {
    console.log('attack-status.component.reloadWorkers(): Started')

    this._clientService.workersAlive().subscribe({
      next: (output: Worker[]) => {
        this.listOfWorkers = output;
        this.listOfClusters = Array.from(new Set(this.listOfWorkers.map(e => e.cluster_id)));
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

  reloadStatus(): void {
    console.log('attack-status.component.reloadStatus(): Started')

    this._clientService.attackOrchestrationStatus().subscribe({
      next: (output: AttackOrchestration) => {
        this.attackOrchestrationStatus = output;
        this.loadingStatus = false;
        this.hasErrorStatus = false;
        this.hasResultStatus = true;
      },
      error: (err) => {
        this.loadingStatus = false;
        this.hasResultStatus = false;
        this.hasErrorStatus = true;
      }
    });
  }

  isStopped(clusterId: string): boolean {
    if (this.attackOrchestrationStatus.goal_akio_by_cluster_id.hasOwnProperty(clusterId) && this.attackOrchestrationStatus.goal_haru_by_cluster_id.hasOwnProperty(clusterId)) {
      let goal_akio = this.attackOrchestrationStatus.goal_akio_by_cluster_id[clusterId];
      let goal_haru = this.attackOrchestrationStatus.goal_haru_by_cluster_id[clusterId];
      let is_haru_disabled = goal_haru.http_flood_target_urls.length == 0;
      let is_akio_disabled = goal_akio.ping_flood_target_ip_address.length == 0 && goal_akio.syn_flood_target_ip_address.length == 0;
      return is_haru_disabled && is_akio_disabled;
    } else {
      return true;
    }
  }
}
