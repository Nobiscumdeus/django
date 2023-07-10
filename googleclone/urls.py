from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('scrape',views.scrape,name='scrape'),
    path('search',views.search_view,name='search'),
    path('count',views.count,name='count'),
    path('counter',views.counter,name='counter'),
    ]