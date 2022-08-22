from django.contrib import admin

# Register your models here.
from Todo.models import TodoItem
admin.site.register(TodoItem)
from Todo.models import Student
admin.site.register(Student)
from Todo.models import Validation
admin.site.register(Validation)
