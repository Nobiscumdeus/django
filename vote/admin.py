from django.contrib import admin

# Register your models here.
from .models import Question
admin.site.register(Question)
from .models import Employee
admin.site.register(Employee)
from .models import Student
admin.site.register(Student)