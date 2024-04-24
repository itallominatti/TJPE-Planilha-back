from django.urls import path

from companies.views.employees import Employees, EmployeeDetail
from companies.views.permissions import PermissionDetail
from companies.views.groups import Groups, GroupDetail

urlpatterns = [
    #Employees Endpoints
    path('employees/', Employees.as_view()),
    path('employees/<int:employee_id>/', EmployeeDetail.as_view()),


    #Groups and permissions endpoints
    path('groups/', Groups.as_view()),
    path('groups/<int:group_id>/', GroupDetail.as_view()),
    path('permissions/', PermissionDetail.as_view()),

]