import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs/internal/Observable";
import {PortscanCheckAllInput} from "../message-protocol/portscan-check-all-input.model";
import {PortscanCheckAllOutput} from "../message-protocol/portscan-check-all-output.model";
import {environment} from "../../environments/environment";

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
}
