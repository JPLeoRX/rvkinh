import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs/internal/Observable";
import {PortscanCheckAllInput} from "../message-protocol/portscan-check-all-input.model";
import {PortscanCheckAllOutput} from "../message-protocol/portscan-check-all-output.model";
import {environment} from "../../environments/environment";
import {PortscanCheckMultipleInput} from "../message-protocol/portscan-check-multiple-input.model";
import {PortscanCheckMultipleOutput} from "../message-protocol/portscan-check-multiple-output.model";

@Injectable({
  providedIn: 'root'
})
export class ClientService {

  constructor(private http: HttpClient) { }

  private _getBaseUrl(): string {
    return environment.controllerUrl;
  }

  private _getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'Api-Key': environment.controllerApiKey
    });
  }

  portscanCheckAll(portscanCheckAllInput: PortscanCheckAllInput): Observable<PortscanCheckAllOutput> {
    // Extract data and prepare it for passing as JSON
    let data = {
      target_ip_address: portscanCheckAllInput.target_ip_address,
    };

    // REST request
    return this.http.post<PortscanCheckAllOutput>(this._getBaseUrl() + '/portscan/check/all', data, {headers: this._getHeaders()});
  }

  portscanCheckMultiple(portscanCheckMultipleInput: PortscanCheckMultipleInput): Observable<PortscanCheckMultipleOutput> {
    // Extract data and prepare it for passing as JSON
    let data = {
      target_ip_address: portscanCheckMultipleInput.target_ip_address,
      list_of_target_ports: portscanCheckMultipleInput.list_of_target_ports,
    };

    // REST request
    return this.http.post<PortscanCheckMultipleOutput>(this._getBaseUrl() + '/portscan/check/multiple', data, {headers: this._getHeaders()});
  }
}
