from django.db import models

class Tjpe(models.Model):
    name = models.CharField(max_length=170)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    tjpe_id = models.ForeignKey(Tjpe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# Create your models here.
