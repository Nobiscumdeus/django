from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse

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
    
   
    
   
    
