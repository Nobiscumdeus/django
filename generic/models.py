import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

#This is created for Questions and set of choices models
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    date_published=models.DateTimeField('Date Published')
    def __str__(self):
        return self.question_text
    '''
    def was_published_recently(self):
        return self.date_published >= timezone.now()-datetime.timedelta(days=1)
        we want to correct the code above so that only past events are recently published and not future ones
    '''
    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.date_published<=now
#People can now make their contributions by selecting their choices here 
class Choice(models.Model):
    #we first collect the question user wants to respond to
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    #we provide the options for choice of texts here 
    choice_text=models.CharField(max_length=200)
    #Options for voting or better still, say selection
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
class TodoList(models.Model):
    name=models.CharField(max_length=200)
    