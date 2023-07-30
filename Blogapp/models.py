from django.db import models
from django.urls import reverse
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#User=get_user_model() #We intend to use the User model for our author

"""
Post Model
Class Post:
id:int
title:varchar:
body:text
-created-at:datetime
modified-at:datetime
"""
    
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=80)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True) #auto_now means it would be updated at a later time 
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__ (self)->str:
        return self.title
    
    def get_absolute_url(self):
        #return reverse('',kwargs={'pk':self.pk})
        return reverse('post_detail',kwargs={'id':self.pk})
    
