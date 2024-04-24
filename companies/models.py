from django.db import models

class Tjpe(models.Model):
    name = models.CharField(max_length=170)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Tjpe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TaskStatus(models.Model):
    name = models.CharField(max_length=155)
    codename = models.CharField(max_length=155)

    class Meta:
        db_table = 'companies_task_status'

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Tjpe, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
