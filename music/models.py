from django.db import models

# Create your models here.
#Red pk 1
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=200)
    album_logo=models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title + ' composed by '+self.artist 
    
class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)   
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250) 
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title
class Members(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    def __str__ (self):
        return self.first_name + ' ' + self.last_name