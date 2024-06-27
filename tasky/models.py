from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission #Helps us to modify the django built in models

from django.contrib.auth.models import Permission

from django.contrib.auth.models import User

# Create your models here.



class Users(AbstractUser):
    SEX_CHOICES=[
       ( 'M','Male'),
        ('F','Female'),
        ('O','Others'),
    ]
    sex=models.CharField(null=True,
        blank=True,max_length=10,
        choices=SEX_CHOICES)
    groups=None
    user_permissions=None
  


class Task(models.Model):
    
    TASK_CHOICES=[
        ('in progress','In Progress'),
        ('completed','Completed'),
        ('overdue','Overdue'),
    ]
    PRIORITY_CHOICES=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]
    
    title=models.CharField(max_length=50)
    description=models.TextField()
    status=models.CharField(null=True,blank=True,max_length=20,choices=TASK_CHOICES)
    priority=models.CharField(null=True,blank=True,max_length=20,choices=PRIORITY_CHOICES)
    due_date=models.DateTimeField()
    category=models.CharField(max_length=100,null=True,blank=True)
    assigned_to=models.ForeignKey(User,on_delete=models.CASCADE)

