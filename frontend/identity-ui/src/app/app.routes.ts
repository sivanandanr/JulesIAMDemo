import { Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard';
import { IdentityListComponent } from './components/identity-list/identity-list';
import { IdentityDetailComponent } from './components/identity-detail/identity-detail';
import { AccessRequestComponent } from './components/access-request/access-request';
import { ConnectorListComponent } from './components/connector-list/connector-list';
import { ConnectorDetailComponent } from './components/connector-detail/connector-detail';
import { SourceListComponent } from './components/source-list/source-list';
import { DiscoveryComponent } from './components/discovery/discovery';
import { LayoutComponent } from './components/layout/layout';

export const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      { path: 'dashboard', component: DashboardComponent },
      { path: 'identities', component: IdentityListComponent },
      { path: 'identities/:id', component: IdentityDetailComponent },
      { path: 'requests', component: AccessRequestComponent },
      { path: 'connectors', component: ConnectorListComponent },
      { path: 'connectors/:id', component: ConnectorDetailComponent },
      { path: 'sources', component: SourceListComponent },
      { path: 'discovery', component: DiscoveryComponent }
    ]
  }
];
