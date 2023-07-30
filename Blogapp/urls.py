app_name="Blogapp"; 
from django.urls import path
from . import views 

urlpatterns=[
    path('',views.home,name='home'),
    path('index',views.index,name='indexpage'),
    path('details/<int:id>/',views.details,name='post_detail'),
    
]
