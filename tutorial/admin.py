from django.contrib import admin

# Register your models here.
from .models import Reporter,Article,Result,Question,Choice
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Result)
admin.site.register(Question)
admin.site.register(Choice)