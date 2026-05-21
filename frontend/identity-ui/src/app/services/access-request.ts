import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Role, Entitlement } from './identity';

export interface WorkflowStep {
  id: number;
  name: string;
  approver: string;
  status: string;
  actionedAt?: string;
}

export interface AccessRequest {
  id?: number;
  requesterId: number;
  requesterName: string;
  identityId: number;
  identityName: string;
  requestType: string;
  targetId: number;
  targetName: string;
  status?: string;
  createdAt?: string;
  comments: string;
  workflowSteps?: WorkflowStep[];
}

@Injectable({
  providedIn: 'root'
})
export class AccessRequestService {
  private apiUrl = 'http://localhost:5283/api'; // Adjusted to match backend port

  constructor(private http: HttpClient) { }

  getRequests(): Observable<AccessRequest[]> {
    return this.http.get<AccessRequest[]>(`${this.apiUrl}/accessrequests`);
  }

  createRequest(request: AccessRequest): Observable<AccessRequest> {
    return this.http.post<AccessRequest>(`${this.apiUrl}/accessrequests`, request);
  }

  approveRequest(id: number): Observable<void> {
    return this.http.put<void>(`${this.apiUrl}/accessrequests/${id}/approve`, {});
  }

  rejectRequest(id: number): Observable<void> {
    return this.http.put<void>(`${this.apiUrl}/accessrequests/${id}/reject`, {});
  }

  getRoles(): Observable<Role[]> {
    return this.http.get<Role[]>(`${this.apiUrl}/roles`);
  }
}
