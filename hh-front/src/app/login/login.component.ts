import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../company.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  logged = false;
  username = '';
  password = '';

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token){
      this.logged = true;
    }
  }

  login(): void {
    this.companyService.login(this.username, this.password)
      .subscribe(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.username = '';
        this.password = '';
      });
  }

  logout(): void {
    localStorage.clear();
    this.logged = false;
  }
}