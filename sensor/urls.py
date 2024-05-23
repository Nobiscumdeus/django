app_name='sensor'
from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserLogOutView
#from django.contrib.auth import views as auth_views


from . import views


urlpatterns=[
    path('register',UserRegistrationView.as_view(),name='register'),
    path('login',UserLoginView.as_view(),name='login'),
    #path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('logout',UserLogOutView.as_view(),name='logout'),
    path('sensor_data_json',views.sensor_data_json,name='sensor_data_json'),
    path('submit_data',views.submit_data,name='submit_data'),
    path('sensor_data_list',views.sensor_data_list,name='sensor_data_list'),
    
]