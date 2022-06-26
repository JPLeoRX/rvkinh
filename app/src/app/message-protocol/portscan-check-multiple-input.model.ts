export class PortscanCheckMultipleInput {
  target_ip_address: string;
  list_of_target_ports: number[];

  constructor(object: any) {
    this.target_ip_address = object.target_ip_address;
    this.list_of_target_ports = object.list_of_target_ports;
  }
}
