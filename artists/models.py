from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	biography = models.TextField(blank=True)

	def get_name_complete(self):
		return "%s %s" % (self.first_name, self.last_name)

	def __unicode__(self):
		return self.first_name