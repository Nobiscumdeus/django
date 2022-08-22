from __future__ import unicode_literals
#This above code must come first
from django.db import models
#Aim is to create an automatic django model form


class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    class Meta:
        db_table="student"


# Create your models here.
class TodoItem(models.Model):
    content=models.TextField()
    
#Django form validation
class Validation(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    econtact=models.CharField(max_length=15)
    class Meta:
        db_table="validation"
    
   
