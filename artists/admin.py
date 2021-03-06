from django.contrib import admin
from .models import Artist

from tracks.models import Track

class TrackInline(admin.StackedInline):
	model = Track
	extra = 1

from albums.models import Album

class AlbumInline(admin.StackedInline):
	model = Album
	extra = 1

class ArtistAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')
	search_fields = ('first_name', 'last_name')
	inlines = [ TrackInline, AlbumInline ]

admin.site.register( Artist , ArtistAdmin )
