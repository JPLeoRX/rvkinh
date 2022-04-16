import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {ClientService} from "../../services/client.service";
import {PortscanCheckAllInput} from "../../message-protocol/portscan-check-all-input.model";
import {PortscanCheckAllOutput} from "../../message-protocol/portscan-check-all-output.model";
import {PortscanCheckMultipleInput} from "../../message-protocol/portscan-check-multiple-input.model";
import {PortscanCheckMultipleOutput} from "../../message-protocol/portscan-check-multiple-output.model";

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
  listOfTargetOpenPorts: number[] = [];

  constructor(private _formBuilder: FormBuilder, private _clientService: ClientService) {
    this.formGroup = this._formBuilder.group({
      target_ip_address: ['', Validators.required],
      target_ports: ['', Validators.required],
    })
  }

  ngOnInit(): void {
  }

  onScanAllCheckbox(): void {
    this.scanAll = !this.scanAll
    if (this.scanAll) {
      this.formGroup.get('target_ports')?.disable();
    } else {
      this.formGroup.get('target_ports')?.enable();
    }
  }

  onFormSubmit(): void {
    if (this.formGroup.valid) {
      this.hasResult = false;
      this.hasError = false;
      this.loading = true;

      if (this.scanAll) {
        let target_ip_address = this.formGroup.value.target_ip_address;
        let portscanCheckAllInput = new PortscanCheckAllInput({
          target_ip_address: target_ip_address,
        });
        console.log(portscanCheckAllInput);

        this._clientService.portscanCheckAll(portscanCheckAllInput).subscribe({
          next: (output: PortscanCheckAllOutput) => {
            this.listOfTargetOpenPorts = output.list_of_target_open_ports;
            console.log(this.listOfTargetOpenPorts)
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

      else {
        let target_ip_address = this.formGroup.value.target_ip_address;
        let target_ports = this.formGroup.value.target_ports;
        let list_of_target_ports = target_ports.replaceAll(" ", "").toLowerCase().split(",")
        let portscanCheckMultipleInput = new PortscanCheckMultipleInput({
          target_ip_address: target_ip_address,
          list_of_target_ports: list_of_target_ports,
        });
        console.log(portscanCheckMultipleInput);

        this._clientService.portscanCheckMultiple(portscanCheckMultipleInput).subscribe({
          next: (output: PortscanCheckMultipleOutput) => {
            this.listOfTargetOpenPorts = output.list_of_target_open_ports;
            console.log(this.listOfTargetOpenPorts)
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
}
