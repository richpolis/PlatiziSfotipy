from django.contrib import admin
from .models import Track
from actions import export_as_excel

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title','artist','order','album','player', 'es_richpolissystems',)
	list_filter = ('artist','album',)
	search_fields = ('title','artist__first_name','artist__last_name',)
	#list_editable = ('title','artist','album')
	actions = (export_as_excel,)
	raw_id_fields = ('artist',)

	def es_richpolissystems(self,obj):
		return obj.id == 1

	es_richpolissystems.boolean = True

admin.site.register( Track, TrackAdmin )