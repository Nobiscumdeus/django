from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Date and Time  of Publication')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
    
class Adeolas(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    def __str__(self):
        return self.firstname
    
class jss1(models.Model):
    fullnames=models.CharField(max_length=200)
    first_test=models.IntegerField(default=0)
    second_test=models.IntegerField(default=0)
    third_test=models.IntegerField(default=0)
    total_tests=models.IntegerField(default=0)
    exams=models.IntegerField(default=0)
    final_scores=models.IntegerField(default=0)
    grades=models.CharField(max_length=1)
    def __str__(self):
        return self.fullnames
   
class jss2(models.Model):
    fullnames=models.CharField(max_length=200)
    first_test=models.IntegerField(default=0)
    second_test=models.IntegerField(default=0)
    third_test=models.IntegerField(default=0)
    total_tests=models.IntegerField(default=0)
    exams=models.IntegerField(default=0)
    final_scores=models.IntegerField(default=0)
    grades=models.CharField(max_length=1)
    def __str__(self):
        return self.fullnames
  
class jss3(models.Model):
    fullnames=models.CharField(max_length=200)
    first_test=models.IntegerField(default=0)
    second_test=models.IntegerField(default=0)
    third_test=models.IntegerField(default=0)
    total_tests=models.IntegerField(default=0)
    exams=models.IntegerField(default=0)
    final_scores=models.IntegerField(default=0)
    grades=models.CharField(max_length=1)
    def __str__(self):
        return self.fullnames
    
class sss1(models.Model):
    fullnames=models.CharField(max_length=200)
    first_test=models.IntegerField(default=0)
    second_test=models.IntegerField(default=0)
    third_test=models.IntegerField(default=0)
    total_tests=models.IntegerField(default=0)
    exams=models.IntegerField(default=0)
    final_scores=models.IntegerField(default=0)
    grades=models.CharField(max_length=1,default='A')
    def __str__(self):
        return self.fullnames
   
class sss2(models.Model):
    fullnames=models.CharField(max_length=200)
    first_test=models.IntegerField(default=0)
    second_test=models.IntegerField(default=0)
    third_test=models.IntegerField(default=0)
    total_tests=models.IntegerField(default=0)
    exams=models.IntegerField(default=0)
    final_scores=models.IntegerField(default=0)
    grades=models.CharField(max_length=1)
    def __str__(self):
        return self.fullnames

    