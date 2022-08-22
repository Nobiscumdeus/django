from django.db import models
from django.utils import timezone

# Create your models here.
class Reporter(models.Model):
    full_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name
class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    
#This was created for a school
class Result(models.Model):
    name=models.CharField(max_length=200)
    student_class=models.CharField(max_length=20)
    term=models.CharField(max_length=10)
    subject=models.CharField(max_length=40)
    score=models.IntegerField()
    grade=models.CharField(max_length=1)
    
    def __str__(self):
        return self.name
    
#This is created for Questions and set of choices models
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    date_published=models.DateTimeField('Date Published')
    def __str__(self):
        return self.question_text
    
    def __was_published_recently(self):
        return self.date_published >= timezone.now()-datetime.timedelta(days=1)

#People can now make their contributions by selecting their choices here 
class Choice(models.Model):
    #we first collect the question user wants to respond to
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    #we provide the options for choice of texts here 
    choice_text=models.CharField(max_length=200)
    #Options for voting or better still, say selection
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.question