from django.urls import path
from . import views 
app_name='apiapp'

urlpatterns = [
    path('',views.firstView.as_view(),name='first'),
    path('ondodoctors',views.OndoDoctorsAPIView.as_view(),name='ondo_doctors'),
    path('church',views.ChurchAPIView.as_view(),name='church'),
    
    
]
