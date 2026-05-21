import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-discovery',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './discovery.html',
  styleUrls: ['./discovery.css']
})
export class DiscoveryComponent {
  discoveryStats = [
    { name: 'Accounts Correlated', count: 1150, color: 'text-green-600', bg: 'bg-green-100' },
    { name: 'Uncorrelated Accounts', count: 42, color: 'text-yellow-600', bg: 'bg-yellow-100' },
    { name: 'Orphan Accounts', count: 15, color: 'text-red-600', bg: 'bg-red-100' },
  ];

  unmatchedAccounts = [
    { accountName: 'svc_backup', source: 'Active Directory', reason: 'Service Account' },
    { accountName: 'temp_user_01', source: 'SAP ERP', reason: 'No Matching Identity' },
    { accountName: 'guest_wifi', source: 'Network', reason: 'Shared Account' },
  ];
}
