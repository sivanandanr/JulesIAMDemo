import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AccessRequestService, AccessRequest } from '../../services/access-request';
import { IdentityService, UserIdentity, Role } from '../../services/identity';

@Component({
  selector: 'app-access-request',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './access-request.html',
  styleUrls: ['./access-request.css']
})
export class AccessRequestComponent implements OnInit {
  requests: AccessRequest[] = [];
  identities: UserIdentity[] = [];
  roles: Role[] = [];

  newRequest: AccessRequest = this.resetRequest();
  showForm = false;

  constructor(
    private requestService: AccessRequestService,
    private identityService: IdentityService
  ) {}

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.requestService.getRequests().subscribe(data => this.requests = data);
    this.identityService.getIdentities().subscribe(data => this.identities = data);
    this.requestService.getRoles().subscribe(data => this.roles = data);
  }

  resetRequest(): AccessRequest {
    return {
      requesterId: 2, // Mocked as Alice Smith
      requesterName: 'Alice Smith',
      identityId: 0,
      identityName: '',
      requestType: 'Role',
      targetId: 0,
      targetName: '',
      comments: ''
    };
  }

  onSubmit(): void {
    const selectedIdentity = this.identities.find(i => i.id == this.newRequest.identityId);
    const selectedRole = this.roles.find(r => r.id == this.newRequest.targetId);

    if (selectedIdentity && selectedRole) {
      this.newRequest.identityName = selectedIdentity.displayName;
      this.newRequest.targetName = selectedRole.name;

      this.requestService.createRequest(this.newRequest).subscribe(() => {
        this.loadData();
        this.showForm = false;
        this.newRequest = this.resetRequest();
      });
    }
  }

  approve(id: number): void {
    this.requestService.approveRequest(id).subscribe(() => this.loadData());
  }

  reject(id: number): void {
    this.requestService.rejectRequest(id).subscribe(() => this.loadData());
  }
}
