from django.urls import path

from api.views import views_cbv
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', views_cbv.CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', views_cbv.CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', views_cbv.VacanciesByCompanyAPIView.as_view()),
    path('vacancies/', views_cbv.VacanciesAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', views_cbv.VacancyDetailApiView.as_view()),
    path('vacancies/top_ten/', views_cbv.TopVacanciesAPIView.as_view())
]

