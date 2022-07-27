from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def index(request):
   return HttpResponse("<h1> Welcome to Django by Nobiscum_deus </h1>")

def setsession(request):
    request.session['sname']='irfan'
    request.session['semail']='irfan.sssit@gmail.com'
    return HttpResponse("session is set")
def getsession(request):
    studentname=request.session['sname']
    studentemail=request.session['semail']
    return HttpResponse(studentname+ " " + studentemail);    
def love(request):
    return HttpResponse("I am the Child of the Almighty")
def nobiscumdeus(request):
    return render(request,"home.html")

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
def home(request):
    return render(request, "vote/home.html")

#create your views 
class SignUp(CreateView):
    form_class =UserCreationForm
    success_url = reverse_lazy("login")
    template_name="registration/signup.html"
    
import csv
def getfile(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="file.csv"'
    writer=csv.writer(response)
    writer.writerow(['1001', 'John', 'Domil', 'CA'])
    writer.writerow(['1002','Amit','Mukharji','LA', '" Testing"'])
    return response

from django.http import HttpResponse
from websiteapp import settings
from django.core.mail import send_mail

def mail(request):
    subject="Greetings"
    msg="Congratulations from Nobiscum_deus for your sucess "
    to ="adeolaolumide99@gmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER, [to])
    if(res==1):
        msg="Mail sent successfully"
    else:
        msg="Mail could not be sent"
    return HttpResponse(msg)

from django.shortcuts import render
from vote.forms import StudentForm

def grace(request):
    student=StudentForm()
    return render(request,"grace.html",{'form':student})

def hello(request):
    return HttpResponse('<h2> Hello welcome Friends -Greetings from Nobiscumdeus </h2>')
    
def brethren(request):
    return HttpResponse("<h1> Continue and do not relent in working on Django ! <br/> - From Nobiscumdeus</h1>")

#Create your views here
import datetime
from django.http import HttpResponse
def decorum(request):
    now=datetime.datetime.now()
    html="<html><body><h3> Now time is %s. </h3></body></html>"%now
    return HttpResponse(html)

#Another function called page
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
def page(request):
    a=1
    if a:
        return HttpResponseNotFound("<h2> Page not Found </h2>")
    else:
        return HttpResponse("<h2> Page was found </h2>")
    
#Working with our Html
from django.shortcuts import render
# used to work with html
from django.template import loader 
from django.http import HttpResponse
def nobiscum(request):
    template=loader.get_template('nobiscum.html')
    return HttpResponse(template.render())

def index(request):
    return render(request,'index.html')

#Working on forms 
from django.shortcuts import render
from vote.forms import StudentForm
def index(request):
    student=StudentForm()
    return render(request,"index.html",{'form':student})

#Instantiating validation forms 
def emp(request):
    if request.method =="POST":
        form=EmployeesForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
        else:
            form=EmployeesForm()
        return render(request,'index.html',{'form':form})
    