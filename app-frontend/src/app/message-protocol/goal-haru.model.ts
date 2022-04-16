import {WorkerHaruSettings} from "./worker-haru-settings.model";

export class GoalHaru {
  http_flood_target_urls: string[];
  worker_settings: WorkerHaruSettings;

  constructor(object: any) {
    this.http_flood_target_urls = object.http_flood_target_urls;
    this.worker_settings = object.worker_settings;
  }
}
