from django.shortcuts import render, get_object_or_404
from .models import Album,Song,Members
def index(request):
    all_albums=Album.objects.all()
    context={
        'all_albums':all_albums
    }
    return render(request,'music/index.html',context)

def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,SongDoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not select a valid song "
        })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})
        

#Trying some new lines
from django.http import HttpResponse
from django.template import loader

def testing(request):
    mydata=Members.objects.all()
    template=loader.get_template('music/members.html')
    context={
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context,request))
    
    
    
        




    