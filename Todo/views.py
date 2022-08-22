from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import datetime
#The code below is used to get the Student form
from Todo.forms import EmpForm
from Todo.forms import StudentForm
from Todo.forms import ValidationForm
#The code below is used to handle uploaded file
from Todo.functions import handle_uploaded_file
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_items=TodoItem.objects.all()
    
    return render(request,'todo/first.html',{'all_items':all_items})

def addTodo(request):
    #create a new to do item collecting the content with the name 
    # save 

    new_item=TodoItem(content=request.POST['content'])
    new_item.save()
    all_items=TodoItem.objects.all()
    
    return render(request,'todo/second.html',{'all_items':all_items})
    #return render(request,'todo/first.html')
    #redirect the browser back to /todo/
def deleteTodo(request,todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
   
    #return HttpResponseRedirect(reverse('todo:addTodo'))
    return HttpResponseRedirect('/todo/')
    


def updatedContent(request):
    updated_content=TodoItem.objects.all()
    return render(request,'todo/updated.html',{'updated_content':updated_content})
    
    #return HttpResponseRedirect(reverse('todo:updatedContent'))

def time(request):
    now=datetime.datetime.now()
    return render(request,'todo/time.html')
    
def index(request):
    stu=EmpForm()
    return render(request,'todo/index.html',{'form':stu})

def application(request):
    student=StudentForm()
    return render(request,"todo/application.html",{'form':student})
   
def validate(request):
    if request.method=="POST":
        form=ValidationForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
        else:
            form=ValidationForm()
        return render(request,'todo/validate.html',{'form':form})
    
def validation(request):
    if request.method=="POST":
        student=StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File Uploaded successfully")
        else:
            student=StudentForm()
            return render(request,"Todo/validate.html",{"form":student})
        
def portfolio(request):
    return render(request,'Todo/portfolio.html')
