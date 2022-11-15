'''
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







urlpatterns=[
    path('<int:album_id>/',views.detail,name='detail'),
    path('',views.detail, name='detail'),
]
'''
#Now we are using the generic view, hence this must change 
from django.conf.urls import url
from . import views

app_name='music'

urlpatterns=[
    #music
    url(r'^$',views.IndexView.as_view(),name='index'),
    #music/712/ >> music/album.id/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),
    #music/album/add
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),
    #music/album/2
    url(r'^(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),
    #music/album/2/delete
    url(r'^(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),
    
    #registration
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
 
  
]
