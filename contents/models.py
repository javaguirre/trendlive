from datetime import datetime

from django.db import models
from django.conf import settings

from networks.models import Network
from events.models import Event, Property


class Content(models.Model):
	ext_id = models.CharField(max_length=250)
	ext_created = models.DateTimeField(null=True, blank=True)
	lang = models.CharField(max_length=10, blank=True)
	created = models.DateTimeField(default=datetime.now(), null=True, blank=True)
	status = models.IntegerField(max_length=1, choices=settings.CONTENT_STATUS, null=False, default=1)
	network_id = models.ForeignKey(Network, null=True, default=0)
	property_id = models.ForeignKey(Property, null=True, default=0)
	important = models.BooleanField(default=False)


class ContentEvent(models.Model):
	event_id = models.ForeignKey(Event)
	content_id = models.ForeignKey(Content)
	status = models.IntegerField(max_length=1, choices=settings.CONTENT_STATUS, null=False, default=1)
