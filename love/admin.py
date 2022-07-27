from django.contrib import admin
from .models import Reporter
from .models import Article
from .models import countries
from .models import Fruit
from .models import Person
from .models import Category
from .models import Product
from .models import Blog
from .models import Author
from .models import Employee

from .models import Entry
# Register your models here.

admin.site.register(Reporter)

admin.site.register(Article)

admin.site.register(countries)

admin.site.register(Fruit)

admin.site.register(Person)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Blog)

admin.site.register(Author)

admin.site.register(Entry)

admin.site.register(Employee)