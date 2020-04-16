import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Company } from './company';
import { Vacancy } from './vacancy';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  constructor(private http: HttpClient) { }

  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>('http://localhost:8000/api/companies/');
  }

  getVacanciesByCompanyId(companyId): Observable<Vacancy[]> {
    const url = `http://localhost:8000/api/companies/${companyId}/vacancies/`;
    return this.http.get<Vacancy[]>(url);
  }
}