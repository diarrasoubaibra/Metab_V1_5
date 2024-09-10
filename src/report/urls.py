from django.urls import path
from report.views.students_report import *
from report.views.users_report import *

app_name = 'report'
urlpatterns = [
    path('', report, name= 'report'),
    path('pdf/<str:report_type>/', generate_pdf_report, name='generate_pdf'),
    path('excel/<str:report_type>/', generate_excel_report, name='generate_excel'),
]