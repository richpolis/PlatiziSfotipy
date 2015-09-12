from random import choice
from tracks.models import Track

frases = ['hola','q','ace']

def basico(request):
	tracks = Track.objects.all()
	
	return {'titulo': choice(frases),}