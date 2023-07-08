from django.urls import path
from . import views

urlpatterns=[
    path('',views.getData),
    path('add',views.addItem),
    path('collect',views.collect,name='collect')
]