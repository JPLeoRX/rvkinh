import { Component, OnInit } from '@angular/core';
import {AttackOrchestration} from "../../message-protocol/attack-orchestration.model";
import {ClientService} from "../../services/client.service";
import {Worker} from "../../message-protocol/worker.model";
import {FormBuilder, FormControl, FormGroup} from "@angular/forms";

@Component({
  selector: 'app-attack',
  templateUrl: './attack.component.html',
  styleUrls: ['./attack.component.css']
})
export class AttackComponent implements OnInit {
  goalSingleEnabled = false;

  hasResultAttackStop: boolean = false;
  hasErrorAttackStop: boolean = false;

  constructor(private _clientService: ClientService) { }

  ngOnInit(): void {
  }

  onGoalSingleCheckbox() {
    this.goalSingleEnabled = !this.goalSingleEnabled
  }

  onStopAttackButton() {
    this._clientService.attackOrchestrationStop().subscribe({
      next: () => {
        this.hasResultAttackStop = true;
        setTimeout(() => {
          this.hasResultAttackStop = false;
        }, 5000);
      },

      error: (err) => {
        this.hasErrorAttackStop = true;
        setTimeout(() => {
          this.hasErrorAttackStop = false;
        }, 5000);
      }
    })
  }
}
