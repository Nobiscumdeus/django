from django.contrib import admin

# Register your models here.
from Todo.models import TodoItem
admin.site.register(TodoItem)
