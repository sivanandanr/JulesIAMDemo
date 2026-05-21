import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IdentityService } from '../../services/identity';
import { AccessRequestService, AccessRequest } from '../../services/access-request';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent implements OnInit {
  identityCount = 0;
  pendingRequestCount = 0;
  recentRequests: AccessRequest[] = [];

  constructor(
    private identityService: IdentityService,
    private requestService: AccessRequestService
  ) {}

  ngOnInit(): void {
    this.identityService.getIdentities().subscribe(identities => {
      this.identityCount = identities.length;
    });

    this.requestService.getRequests().subscribe(requests => {
      this.recentRequests = requests.slice(0, 5);
      this.pendingRequestCount = requests.filter(r => r.status === 'Pending').length;
    });
  }
}
