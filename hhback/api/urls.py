from django.urls import path

from api.views import company_list, company_details, vacancies_company, vacancy_list, vacancy_details, top_ten

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_details),
    path('companies/<int:id>/', vacancies_company),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_details),
    path('vacancies/top_ten/',top_ten)

]
