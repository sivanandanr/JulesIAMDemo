import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { IdentityService, UserIdentity } from '../../services/identity';

@Component({
  selector: 'app-identity-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './identity-detail.html',
  styleUrls: ['./identity-detail.css']
})
export class IdentityDetailComponent implements OnInit {
  identity?: UserIdentity;

  constructor(
    private route: ActivatedRoute,
    private identityService: IdentityService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.identityService.getIdentity(id).subscribe(data => {
      this.identity = data;
    });
  }
}
