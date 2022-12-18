from django.urls import path 
#from django.conf.urls import include,url
from . import views 
app_name='todo'

urlpatterns=[
    #path('',views.todoView,name='todoView'),
    #path('addTodo/',views.addTodo,name='addTodo'),
    
    #url(r'^$',views.todoView,name='todoView'),
    #url(r'^addTodo/$',views.addTodo,name='addTodo'),
   
    path('addTodo/deleteTodo/<int:todo_id>/',views.deleteTodo,name='deleteTodo'),
    path('updated/',views.updatedContent,name='updatedContent'),
    path('addTodo',views.addTodo,name='addTodo'),
    path('time/',views.time,name="time"),
    path('index/',views.index,name='index'),
    path('application/',views.application,name='application'),
    path('portfolio/',views.portfolio,name='portfolio'),
    
    
  
  
]