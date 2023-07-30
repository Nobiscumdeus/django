from django.urls import path
from . import views
app_name='love'

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    path('',views.first,name='first'),
    path('articles',views.article_list,name='article_list'),
    path('articles/<int:id>',views.article_details,name='article_details'),
]

#To kind of allow further extensions in the url patterns
urlpatterns=format_suffix_patterns(urlpatterns)