from rest_framework.views import APIView

from companies.utils.exceptions import NotFoundEmploeey, NotFoundGroup, NotFoundTask, NotFoundTaskStatus, RequiredFields
from companies.models import Employee, Task, TaskStatus, Tjpe

from accounts.models import Group

class Base(APIView):
    def get_enterprise_id(self, user_id) -> int:
        employee = Employee.objects.filter(user_id=user_id).first()
        owner = Tjpe.objects.filter(user_id=user_id).first()

        if employee:
            return employee.enterprise_id
        
        return owner.id

    def get_employee(self, employee_id, user_id) -> Employee:
        enterprise_id = self.get_enterprise_id(user_id)

        employee = Employee.objects.filter(id=employee_id, enterprise_id=enterprise_id).first()

        if not employee:
            raise NotFoundEmploeey()

        return employee

    def get_group(self, group_id, enterprise_id) -> Group:
        group = Group.objects.values('name').filter(id=group_id, enterprise_id=enterprise_id).first()

        if not group:
            raise NotFoundGroup()

        return group
    
    def get_status (self, status_id) -> TaskStatus:
        status = TaskStatus.objects.filter(id=status_id).first()

        if not status:
            raise NotFoundTaskStatus()

        return status
    
    def get_task(self, task_id, enterprise_id) -> Task:
        task = Task.objects.filter(id=task_id, enterprise_id=enterprise_id).first()

        if not task:
            raise NotFoundTask()

        return task

    ...