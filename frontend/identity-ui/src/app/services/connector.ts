import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Application {
  id: number;
  name: string;
  description: string;
  isTrustedSource: boolean;
}

export interface Connector {
  id: number;
  name: string;
  type: string;
  host: string;
  status: string;
  provisioningConfig: string;
  applications: Application[];
}

@Injectable({
  providedIn: 'root'
})
export class ConnectorService {
  private apiUrl = 'http://localhost:5283/api'; // Adjusted to match backend port

  constructor(private http: HttpClient) { }

  getConnectors(): Observable<Connector[]> {
    return this.http.get<Connector[]>(`${this.apiUrl}/connectors`);
  }

  getConnector(id: number): Observable<Connector> {
    return this.http.get<Connector>(`${this.apiUrl}/connectors/${id}`);
  }

  updateProvisioning(id: number, config: string): Observable<void> {
    return this.http.put<void>(`${this.apiUrl}/connectors/${id}/provisioning`, `"${config}"`, {
      headers: { 'Content-Type': 'application/json' }
    });
  }

  getTrustedSources(): Observable<Application[]> {
    return this.http.get<Application[]>(`${this.apiUrl}/sources`);
  }

  aggregate(id: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/sources/${id}/aggregate`, {});
  }
}
