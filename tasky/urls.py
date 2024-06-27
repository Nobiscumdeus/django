from django.urls import path 
from . import views 
from .views import TaskListView,TaskUpdateView,TaskCreateView,TaskDeleteView,TaskDetailView

app_name='tasky'


'''
The  End points for our tasks 
'''
urlpatterns=[
    path('dashboard',views.dashboard,name='dashboard'),
    path('responsive',views.responsive,name='responsive'),
    path('task',TaskListView.as_view(),name='task-list'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('task/new/',TaskCreateView.as_view(),name='task-create'),
    path('task/<int:pk>/edit/',TaskUpdateView.as_view(),name='task-update'),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(),name='task-delete'),
  
         
]