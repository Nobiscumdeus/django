from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request,'blogapp/base.html')

def index(request):
    posts=Post.objects.all()
    return render(request,'blogapp/index.html',{'posts':posts})
def details(request,id):
    detail=Post.objects.filter(pk=id)
    context={
        'detail':detail,
    }
    return render(request,'blogapp/detail.html',context)
