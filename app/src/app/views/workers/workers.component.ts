import { Component, OnInit } from '@angular/core';
import {ClientService} from "../../services/client.service";
import {Worker} from "../../message-protocol/worker.model";
import {PortscanCheckMultipleOutput} from "../../message-protocol/portscan-check-multiple-output.model";

@Component({
  selector: 'app-workers',
  templateUrl: './workers.component.html',
  styleUrls: ['./workers.component.css']
})
export class WorkersComponent implements OnInit {
  loading: boolean = false;
  hasResult: boolean = false;
  hasError: boolean = false;
  listOfWorkers: Worker[] = []
  // listOfWorkers: Worker[] = [
  //   new Worker({cluster_id: "ano", worker_id: "worker1"}),
  //   new Worker({cluster_id: "ano", worker_id: "worker2"}),
  //   new Worker({cluster_id: "ano", worker_id: "worker3"}),
  //
  //   new Worker({cluster_id: "google-cloud", worker_id: "hungry_mendel"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "happy_raman"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "ecstatic_williams"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "kind_wiles"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "focused_antonelli"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "hungry_mendel"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "happy_raman"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "ecstatic_williams"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "kind_wiles"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "focused_antonelli"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "hungry_mendel"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "happy_raman"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "ecstatic_williams"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "kind_wiles"}),
  //   new Worker({cluster_id: "google-cloud", worker_id: "focused_antonelli"}),
  // ]
  listOfClusters: string[] = []
  // listOfClusters: string[] = ["ano", "google-cloud"]

  constructor(private _clientService: ClientService) { }

  ngOnInit(): void {
    this.loadWorkers();

    setInterval(() => {
      this.reloadWorkers();
    }, 6000)
  }

  loadWorkers() {
    console.log('workers.component.loadWorkers(): Started')
    this.hasResult = false;
    this.hasError = false;
    this.loading = true;

    this._clientService.workersAlive().subscribe({
      next: (output: Worker[]) => {
        this.listOfWorkers = output;
        this.listOfClusters = Array.from(new Set(this.listOfWorkers.map(e => e.cluster_id)));
        this.loading = false;
        this.hasError = false;
        this.hasResult = true;
      },
      error: (err) => {
        this.loading = false;
        this.hasResult = false;
        this.hasError = true;
      }
    });
  }

  reloadWorkers() {
    console.log('workers.component.reloadWorkers(): Started')

    this._clientService.workersAlive().subscribe({
      next: (output: Worker[]) => {
        this.listOfWorkers = output;
        this.listOfClusters = Array.from(new Set(this.listOfWorkers.map(e => e.cluster_id)));
        this.loading = false;
        this.hasError = false;
        this.hasResult = true;
      },
      error: (err) => {
        this.loading = false;
        this.hasResult = false;
        this.hasError = true;
      }
    });
  }
}
