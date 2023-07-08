"""websiteapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



""""
from django.contrib import admin
from django.urls import path
from vote import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello', views.hello),
]


urlpatterns=[
    path('admin/', admin.site.urls),
    path('love',views.love),
]

urlpatterns=[
    path('vote/', include('vote.urls')),
    path('admin/',admin.site.urls),
]
urlpatterns=[
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('ssession',views.setsession),
    path('gsession', views.getsession),
    path('love',views.love),
    path('nobiscumdeus',views.nobiscumdeus),
    
]
from django.urls import path,include
urlpatterns=[
    path('admin/',admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('home/',include('vote.urls')),
]

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',include('TechnicalCourses.urls')),
]
urlpatterns=[
    path('admin/',admin.site.urls),
    path('csv',views.getfile),
]
urlpatterns=[
    path('admin/',admin.site.urls),
    path('mail',views.mail),
]
from django.contrib import admin
from django.urls import path
from vote import views
#for apps in views of vote
urlpatterns=[
      
    path('admin/',admin.site.urls),
    path('brethren',views.brethren),
    path('love',views.love),
    path('decorum',views.decorum),
    path('page/',views.page),
    path('grace/',views.grace),
    path('hello',views.hello),
    path('index',views.index),
    
    
]
#Working on html in particular
from django.contrib import admin
from django.urls import path
from love import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('welcome',views.welcome),
]


"""






#Working with the polls database
from django.contrib import admin
from django.urls import include, path


# working with the accounts database
urlpatterns=[
    #for the general admin page
    path('admin/',admin.site.urls),
    #for dictionary app so that both can at least work at the same time when called 
    path('polls/', include('polls.urls')),
    path('vote/',include('vote.urls')), 
    path('music/',include('music.urls')),
    path('todo/',include('Todo.urls')),
    path('api/',include('api.urls')),
    path('tutorial/',include('tutorial.urls')),
    path('generic/',include('generic.urls')),
    path('apiapp/',include('apiapp.urls')),
    #path('api-auth/',include('rest-framework.urls')),
 
]


    
