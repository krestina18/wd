import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../vacancy';
import { CompanyService } from '../company.service';

@Component({
  selector: 'app-topten',
  templateUrl: './topten.component.html',
  styleUrls: ['./topten.component.css']
})
export class ToptenComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.getTopTen();
  }

  getTopTen(): void {
    this.companyService.getTopTen().subscribe(vacancies => this.vacancies = vacancies);
  }
}
