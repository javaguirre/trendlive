from django.db import models

# Create your models here.

class Property(models.Model):
	TYPES = (('profile', 'Profile'), ('tag', 'Hashtag'))
	
	value = models.CharField(max_length=250)
	type = models.CharField(max_length=10, choices=TYPES, null=False, default='tag')
	status = models.IntegerField(max_length=1, choices=settings.CONTENT_STATUS, null=False, default=1)
	network_id = models.ForeignKey(Network, null=True, default=0)
	important = forms.BooleanField(initial=False)


class PropertyEvent(models.Model):
	event_id = models.ForeignKey(Event)
	property_id = models.ForeignKey(Property)
	status = models.IntegerField(max_length=1, choices=settings.CONTENT_STATUS, null=False, default=1)
	