from django.contrib import admin

# Register your models here.
from .models import Task,Users
admin.site.register(Task)
admin.site.register(Users)