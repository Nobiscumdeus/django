#Here we intend to use the generic view
from django.urls import path
from . import views 
app_name="generic"

#Note that the main purpose of creating this is to experiment the generic view 
urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    #The pk here just represents the id directly
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results',views.ResultView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    
    #for forms 
    
    path('form/',views.home,name='home'),
    
    
    
]