from django.db import models

# Create your models here.
class Destination(models.Model):
    TaskName = models.CharField(max_length=100)
    DueDate = models.DateField(auto_now=False,auto_now_add=False)