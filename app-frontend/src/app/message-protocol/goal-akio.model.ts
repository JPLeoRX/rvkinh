export class GoalAkio {
  ping_flood_target_ip_address: string;
  syn_flood_target_ip_address: string;
  syn_flood_target_port: number;

  constructor(object: any) {
    this.ping_flood_target_ip_address = object.ping_flood_target_ip_address;
    this.syn_flood_target_ip_address = object.syn_flood_target_ip_address;
    this.syn_flood_target_port = object.syn_flood_target_port;
  }
}
