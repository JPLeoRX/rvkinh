export class Worker {
  cluster_id: string;
  worker_id: string;

  constructor(object: any) {
    this.cluster_id = object.cluster_id;
    this.worker_id = object.worker_id;
  }
}
