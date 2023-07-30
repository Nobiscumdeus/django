from django.urls import path
from . import views
app_name='Blogappusers'

urlpatterns=[
    path('signingup',views.register_user,name='signup_page'),
    path('login',views.login_page,name="login_page"),
    
    
    
    
    
    
    
    
]