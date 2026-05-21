import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Entitlement {
  id: number;
  name: string;
  type: string;
  description: string;
}

export interface Role {
  id: number;
  name: string;
  description: string;
  entitlements: Entitlement[];
}

export interface UserIdentity {
  id: number;
  username: string;
  displayName: string;
  email: string;
  status: string;
  department: string;
  jobTitle: string;
  roles: Role[];
}

@Injectable({
  providedIn: 'root'
})
export class IdentityService {
  private apiUrl = 'http://localhost:5283/api/identities'; // Adjusted to match backend port

  constructor(private http: HttpClient) { }

  getIdentities(): Observable<UserIdentity[]> {
    return this.http.get<UserIdentity[]>(this.apiUrl);
  }

  getIdentity(id: number): Observable<UserIdentity> {
    return this.http.get<UserIdentity>(`${this.apiUrl}/${id}`);
  }

  updateStatus(id: number, status: string): Observable<void> {
    return this.http.put<void>(`${this.apiUrl}/${id}/status`, `"${status}"`, {
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
