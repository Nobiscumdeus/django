app_name='sensor'
from django.urls import path

from . import views


urlpatterns=[
    path('submit_data',views.submit_data,name='submit-data'),
]