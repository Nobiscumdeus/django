from django.urls import path
from . import views 
app_name='apiapp'

urlpatterns = [
    path('',views.firstView.as_view(),name='first'),
    
    
]
