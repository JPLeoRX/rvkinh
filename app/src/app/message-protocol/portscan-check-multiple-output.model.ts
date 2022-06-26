export class PortscanCheckMultipleOutput {
  target_ip_address: string;
  list_of_target_ports: number[];
  list_of_target_open_ports: number[];

  constructor(object: any) {
    this.target_ip_address = object.target_ip_address;
    this.list_of_target_ports = object.list_of_target_ports;
    this.list_of_target_open_ports = object.list_of_target_open_ports;
  }
}
