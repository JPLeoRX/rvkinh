export class WorkerHaruSettings {
  parallel_min_requests: number;
  parallel_max_requests: number;
  proxy_type: string;
  proxy_ip_change_frequency: number;

  constructor(object: any) {
    this.parallel_min_requests = object.parallel_min_requests;
    this.parallel_max_requests = object.parallel_max_requests;
    this.proxy_type = object.proxy_type;
    this.proxy_ip_change_frequency = object.proxy_ip_change_frequency;
  }
}
