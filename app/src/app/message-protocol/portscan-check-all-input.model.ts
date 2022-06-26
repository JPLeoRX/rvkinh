export class PortscanCheckAllInput {
  target_ip_address: string;

  constructor(object: any) {
    this.target_ip_address = object.target_ip_address;
  }
}
