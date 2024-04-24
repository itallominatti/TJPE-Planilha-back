from django.urls import path

from companies.views.employees import Employees, EmployeeDetail
from companies.views.permissions import PermissionDetail

urlpatterns = [
    #Employees Endpoints
    path('employees/', Employees.as_view()),
    path('employees/<int:employee_id>/', EmployeeDetail.as_view()),


    #Groups and permissions endpoints
    path('permissions/', PermissionDetail.as_view()),

]