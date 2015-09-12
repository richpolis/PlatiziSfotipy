from random import choice
from tracks.models import Track

frases = ['hola','q','ace']

def basico(request):
	tracks = Track.objects.all()
	track = None
	# import ipdb; ipdb.set_trace()
	for t in tracks:
		if request.path == t.get_absolute_url():
			track = t
			break

	# import ipdb; ipdb.set_trace()
	return { 'titulo': choice(frases), 'tracks': tracks, 'selected_track': track }