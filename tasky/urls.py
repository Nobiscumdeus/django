from django.urls import path 
from . import views 
from .views import (TaskUpdateView,TaskCreateView,TaskDetailView,
                    RegisterView,LoginView
                    
                   )
from . import views

app_name='tasky'


'''
The  End points for our tasks 
'''
urlpatterns=[
    path('',views.home,name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login',LoginView.as_view(),name='login'),
    path('dashboard/',views.task_list_view,name='dashboard'),
    
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('task/new/',TaskCreateView.as_view(),name='task-create'),
    
    path('task/<int:pk>/edit/',TaskUpdateView.as_view(),name='task-update'),
    
    path('task/<int:pk>/delete/', views.task_delete_view, name='task-delete'),
   
   
         
]