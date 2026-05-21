import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ConnectorService, Connector } from '../../services/connector';

@Component({
  selector: 'app-connector-detail',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './connector-detail.html',
  styleUrls: ['./connector-detail.css']
})
export class ConnectorDetailComponent implements OnInit {
  connector?: Connector;
  configJson: string = '';

  constructor(
    private route: ActivatedRoute,
    private connectorService: ConnectorService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.connectorService.getConnector(id).subscribe(data => {
      this.connector = data;
      this.configJson = data.provisioningConfig;
    });
  }

  saveConfig(): void {
    if (this.connector) {
      this.connectorService.updateProvisioning(this.connector.id, this.configJson).subscribe(() => {
        alert('Configuration saved successfully');
      });
    }
  }
}
