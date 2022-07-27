from django.conf.urls import include,url
from . import views 
from django.urls import path

app_name='music'

urlpatterns=[
  #music
     #url(r'^$',views.index, name='index'),
     path('',views.index,name='index'),
    
     
    
    # url(r'^(?P<album_title>[0-9]+)$',views.detail,name='detail'),
    
]


'''urlpatterns=[
    path('<int:album_id>/',views.detail,name='detail'),
    path('',views.detail, name='detail'),
]
'''

#Trying the url pattern
urlpatterns=[
    #music
    url(r'^$',views.index,name='index'),
    #music/712/ >> music/album.id/
   url(r'^(?P<album_id>[0-9]+)/$',views.detail,name="detail"),
 
    #music/album.id/favorite
     url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name="favorite"),
   path('members/',views.testing,name='testing'),
]
