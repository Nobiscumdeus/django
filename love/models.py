from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
from django.db import models
class Person(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    
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
    
class Runner(models.Model):
    MedalType=models.TextChoices('MedalType','GOLD SILVER BRONZE')
    name=models.CharField(max_length=70)
    medal=models.CharField(blank=True,choices=MedalType.choices,max_length=10)
class Fruit(models.Model):
    name=models.CharField(max_length=70, primary_key=True)
class countries(models.Model):
    country=models.CharField(max_length=100)
    capital=models.CharField(max_length=100)
               
               
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desctiption=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return '{}'.format(self.name)
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return '{}'.format(self.name)
    
  
class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()
    def __str__(self):
        return self.name
        
class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    def __str__(self):
        return self.name
class Entry(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField(default=date.today)
    authors=models.ManyToManyField(Author)
    number_of_comments=models.IntegerField(default=0)
    number_of_pingbacks=models.IntegerField(default=0)
    rating=models.IntegerField(default=5)
    def __str__(self):
        return self.headline
            
class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=15)
    class Meta:
        db_table="employe"
        
    