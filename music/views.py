'''from django.shortcuts import render, get_object_or_404
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
    except(KeyError,Song.DoesNotExist):
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
'''                                                     
    # We now intend to make use of the genric vuew instead
from django.views import generic
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from music.forms import UserForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='all_albums'
    #note that the result of the query is often stored as object_list which we now use in our index
    #We can overwrite by resetting the context_object_name
    
    def get_queryset(self):
        return Album.objects.all()
    
class DetailView(generic.DetailView):
    model=Album
    template_name='music/detail.html'
    context_object_name='album'


class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']
class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']
    
class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('music:index')
    
class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'
    
    def get(self,request):
        form=self.form_class(None)
        return render(self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)
        
        if form.is_valid():
            user=form.save(commit=False)
            #cleaned or normalized data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #returns user objects if credentials are correct
            user=authenticate(username=username,password=password)
            
            if user is not None:
                if user.is_active():
                    login(request,user)
                    return redirect('music:index')
                
        return render(request,self.template_name,{'form':form})
            
    
    
    
    
    
    
    
    
    
    
    
    



    