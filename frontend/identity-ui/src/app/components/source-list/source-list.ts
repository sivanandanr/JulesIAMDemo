import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConnectorService, Application } from '../../services/connector';

@Component({
  selector: 'app-source-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './source-list.html',
  styleUrls: ['./source-list.css']
})
export class SourceListComponent implements OnInit {
  sources: Application[] = [];
  aggregatingIds = new Set<number>();

  constructor(private connectorService: ConnectorService) {}

  ngOnInit(): void {
    this.connectorService.getTrustedSources().subscribe(data => this.sources = data);
  }

  aggregate(id: number): void {
    this.aggregatingIds.add(id);
    this.connectorService.aggregate(id).subscribe(res => {
      alert(res.message + ': ' + res.identitiesProcessed + ' identities processed');
      this.aggregatingIds.delete(id);
    });
  }
}
