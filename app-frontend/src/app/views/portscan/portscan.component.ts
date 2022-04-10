import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from "@angular/forms";
import {ClientService} from "../../services/client.service";
import {PortscanCheckAllInput} from "../../message-protocol/portscan-check-all-input.model";
import {PortscanCheckAllOutput} from "../../message-protocol/portscan-check-all-output.model";

@Component({
  selector: 'app-portscan',
  templateUrl: './portscan.component.html',
  styleUrls: ['./portscan.component.css']
})
export class PortscanComponent implements OnInit {
  loading: boolean = false;
  scanAll: boolean = false;
  formGroup: FormGroup;
  hasResult: boolean = false;
  hasError: boolean = false;
  list_of_target_open_ports: number[] = [];

  constructor(private _formBuilder: FormBuilder, private _clientService: ClientService) {
    this.formGroup = this._formBuilder.group({
      target_ip_address: []
    })
  }

  ngOnInit(): void {
  }

  onScanAllCheckbox(): void {
    this.scanAll = !this.scanAll
  }

  onFormSubmit(): void {
    this.hasResult = false;
    this.hasError = false;
    this.loading = true;

    if (this.scanAll) {
      let target_ip_address = this.formGroup.value.target_ip_address;
      let portscanCheckAllInput = new PortscanCheckAllInput({
        target_ip_address: target_ip_address,
      });
      console.log(portscanCheckAllInput)

      this._clientService.portscanCheckAll(portscanCheckAllInput).subscribe({
        next: (output: PortscanCheckAllOutput) => {
          this.list_of_target_open_ports = output.list_of_target_open_ports;
          console.log(this.list_of_target_open_ports)
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
}
