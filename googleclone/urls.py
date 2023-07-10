from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('scrape',views.scrape,name='scrape'),
    path('google',views.open_search,name='open_search'),
    path('search',views.search,name='search'),
    path('count',views.count,name='count'),
    path('counter',views.counter,name='counter'),
    path('search_view',views.search_view,name='search_view')
    ]