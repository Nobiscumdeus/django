from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def indexView(request):
    return render(request,'accounts/index.html')
@login_required

def dashboardView(request):
    return render(request,'accounts/dashboard.html')

def registerView(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        #It returns user to login page if account creation is successfull
    else:
        form=UserCreationForm()
    return render(request,'accounts/register.html',{'form':form})
    
    
def loginView(request):
    return render(request,'')

