from django.db import models

class Tjpe(models.Model):
    name = models.CharField(max_length=170)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
# Create your models here.
