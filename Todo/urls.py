from django.urls import path 
from django.conf.urls import include,url
from . import views 
app_name='todo'

urlpatterns=[
    #path('',views.todoView,name='todoView'),
    #path('addTodo/',views.addTodo,name='addTodo'),
    url(r'^$',views.todoView,name='todoView'),
    url(r'^addTodo/$',views.addTodo,name='addTodo'),
    #url(r'addTodo/deleteTodo/<int:todo_id>/$',views.deleteTodo,name='deleteTodo'),
    path('addTodo/deleteTodo/<int:todo_id>/',views.deleteTodo,name='deleteTodo'),
    path('updated/',views.updatedContent,name='updatedContent'),
    path('addTodo',views.addTodo,name='addTodo'),
    
    
  
  
]