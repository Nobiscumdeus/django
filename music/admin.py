from django.contrib import admin

# Register your models here.
from .models import Album
admin.site.register(Album)

from .models import Song
admin.site.register(Song)

from .models import Members
admin.site.register(Members)
