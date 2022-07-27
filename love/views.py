from django.shortcuts import render

# Create# your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse("This is first function powered by Nobiscumdeus ")
def welcome(request):
    return HttpResponse("Hello world , welcome to Django by Nobiscumdeus ")
