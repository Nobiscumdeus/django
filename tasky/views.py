from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy 
from .models import Task
from .forms import TaskForm,EditTaskForm
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UsersCreationForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import login,authenticate,logout
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'tasky/base.html')

@login_required
def dashboard(request):
    return render(request,'tasky/dashboard.html')


@login_required
def task_list_view(request):
    in_progress_tasks = Task.objects.filter(status='in progress').order_by('-due_date')
    completed_tasks = Task.objects.filter(status='completed').order_by('-due_date')
    overdue_tasks = Task.objects.filter(status='overdue').order_by('-due_date')

    context = {
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
    }

    return render(request, 'tasky/dashboard.html', context)

class RegisterView(CreateView,LoginRequiredMixin):
    model = User
    form_class = UsersCreationForm
    template_name = 'tasky/register.html'
    success_url = reverse_lazy('tasky:dashboard')
    
    
class TaskCreateView(CreateView,LoginRequiredMixin):
    model=Task
    form_class=TaskForm
    template_name='tasky/add_task.html'
    context_object_name='task_create'
    success_url=reverse_lazy('tasky:dashboard')
    
    
class TaskDetailView(DetailView,LoginRequiredMixin):
    model=Task
    template_name='tasky/detail.html'
    context_object_name='task_detail'
    
    
class TaskUpdateView(UpdateView,LoginRequiredMixin):
    model=Task
    template_name='tasky/edit_task.html'
    form_class=EditTaskForm
    success_url=reverse_lazy('tasky:dashboard')
    
    
@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse_lazy('tasky:dashboard'))
    return render(request, 'tasky/confirm_delete.html', {'task': task})

class LoginView(View):
    template_name='tasky/login.html'
    def get(self,request,*args,**kwargs):
        form=UserLoginForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                
                return redirect('tasky:dashboard')
            else:
                # Invalid login
                pass
        return render(request,self.template_name,{'form':form})
        
### The Custom Logout Function 
class CustomLogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('tasky:home')   




#### Search View 


from django.http import JsonResponse
from .forms import SearchForm

def search_view(request):
    # Check if the request method is GET and if it's an AJAX request
    if request.method == "GET" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchForm(request.GET)  # Bind the form with GET data
        if form.is_valid():
            # Extract form data
            query = form.cleaned_data.get('query')
            sort_by = form.cleaned_data.get('sort_by')
            status = form.cleaned_data.get('status')
            priority = form.cleaned_data.get('priority')

            # Get all tasks
            tasks = Task.objects.all()

            # Apply filters
            if query:
                tasks = tasks.filter(title__icontains=query)
            if status:
                tasks = tasks.filter(status=status)
            if priority:
                tasks = tasks.filter(priority=priority)
            if sort_by:
                tasks = tasks.order_by(sort_by)

            # Prepare results
            results = [
                {
                    'title': task.title,
                    'description': task.description,
                    'due_date': task.due_date,
                    'priority': task.get_priority_display(),
                    'status': task.get_status_display(),
                    'category': task.category,
                    'assigned_to': task.assigned_to.username,
                }
                for task in tasks
            ]
            return JsonResponse({'results': results})  # Return JSON response
    else:
        form = SearchForm()  # Create an empty form if not an AJAX request
    return render(request, 'tasky/search.html', {'form': form})  # Render the template with the form



def search(request):
    return render(request,'tasky/search.html')