import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ConnectorService, Connector } from '../../services/connector';

@Component({
  selector: 'app-connector-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './connector-list.html',
  styleUrls: ['./connector-list.css']
})
export class ConnectorListComponent implements OnInit {
  connectors: Connector[] = [];

  constructor(private connectorService: ConnectorService) {}

  ngOnInit(): void {
    this.connectorService.getConnectors().subscribe(data => this.connectors = data);
  }
}
