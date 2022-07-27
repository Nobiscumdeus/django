from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Allcourses
from django.template import loader

def Courses(request):
    ac=Allcourses.objects.all()
    template=loader.get_template('/TechnicalCourses/Courses.html')
    context={
        'ac':ac,
        
    }
    return HttpResponse(template.render(context, request))

def detail(request,course_id):
    return HttpResponse('<h2> These are the course details for course id ' +str(course_id) + '</h2>')