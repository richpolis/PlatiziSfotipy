import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Track

def homepage(request):
	return render(request,'homepage.html')

# response views template
#def track_view(request, title):
#	track = get_object_or_404(Track, title=title)
#	return render(request, 'track.html',{'track': track})

# response json
def track_view(request, title):
	track = get_object_or_404(Track, title=title)

	data = {
		'id': track.id,
		'title': track.title,
		'order': track.order,
		'album': {
			'id': track.album.id,
			'title': track.album.title
		},
		'artist': {
			'id': track.artist.id,
			'name': track.artist.first_name,
			'biography': track.artist.biography
		}
	}

	json_data = json.dumps(data)

	#return HttpResponse(json_data,content_type='application/json')
	return render(request,'track.html',{'track': track})