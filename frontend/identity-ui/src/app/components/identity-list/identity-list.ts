import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { IdentityService, UserIdentity } from '../../services/identity';

@Component({
  selector: 'app-identity-list',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './identity-list.html',
  styleUrls: ['./identity-list.css']
})
export class IdentityListComponent implements OnInit {
  identities: UserIdentity[] = [];
  filteredIdentities: UserIdentity[] = [];
  searchTerm: string = '';

  constructor(private identityService: IdentityService) {}

  ngOnInit(): void {
    this.identityService.getIdentities().subscribe(data => {
      this.identities = data;
      this.filteredIdentities = data;
    });
  }

  onSearch(): void {
    const term = this.searchTerm.toLowerCase();
    this.filteredIdentities = this.identities.filter(i =>
      i.displayName.toLowerCase().includes(term) ||
      i.username.toLowerCase().includes(term) ||
      i.email.toLowerCase().includes(term)
    );
  }

  getStatusClass(status: string): string {
    switch (status) {
      case 'Active': return 'bg-green-100 text-green-800';
      case 'Inactive': return 'bg-yellow-100 text-yellow-800';
      case 'Terminated': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  }
}
