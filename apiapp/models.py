from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Church(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=250)
    founder=models.CharField(max_length=250)
    
class OndoDoctors(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=250)
    birth_day=models.CharField(max_length=300)
    specialty=models.CharField(max_length=300)
    local_govt=models.CharField(max_length=200)
    medical_school=models.CharField(max_length=200)
    hospital_worked=models.CharField(max_length=200)
    positions=models.CharField(max_length=300)
    awards=models.CharField(max_length=200)
    
    
    