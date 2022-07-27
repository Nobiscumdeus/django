from django.db import models
import datetime
from django.db import models
from django.utils import timezone 

# Create your models here.
class Question(models.Model):
    def __str__ (self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
class Choice(models.Model):
    def __str__ (self):
        return self.choice_text
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
class Employee(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=30)
    release_date=models.DateField()
    num_stars=models.IntegerField()
class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    contact=models.IntegerField()
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    
#working on django forms 
from django.db import models
class Employees(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    econtact=models.CharField(max_length=15)
    class Meta:
        db_table="employee"

