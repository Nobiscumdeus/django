from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy 
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# Create your views here.

def dashboard(request):
    return render(request,'tasky/dashboard.html')

def responsive(request):
    return render(request,'tasky/responsive.html')


class TaskListView(ListView):
    model=Task
    template_name='tasky/dashboard.html'
    context_object_name='task_list'
    
    
class TaskCreateView(CreateView):
    model=Task
    form_class=TaskForm
    template_name='tasky/add_task.html'
    context_object_name='task_create'
    success_url=reverse_lazy('tasky:dashboard')
class TaskDetailView(DetailView):
    model=Task
    template_name='tasky/dashboard.html'
    context_object_name='task_detail'
    
    
class TaskUpdateView(UpdateView):
    model=Task
    template_name='tasky/dashboard.html'
    fields='__all__'
    success_url=reverse_lazy('tasky:dashboard')
    
    
class TaskDeleteView(DeleteView):
    model=Task
    template_name='tasky/confirm_delete.html'
    success_url='tasky:dashboard'
    


class TaskListByStatus(generics.ListAPIView):
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    
    
    def get_queryset(self):
        status=self.request.query_params.get('status',None)
        if status is not None:
            return Task.objects.filter(status=status)
        return Task.objects.all()
    
    

