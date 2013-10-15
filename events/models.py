from datetime import datetime
from django.conf import settings

from django.db import models

from networks.models import Network


class Property(models.Model):
    TYPES = (('profile', 'Profile'), ('tag', 'Hashtag'))

    value = models.CharField(max_length=250)
    type = models.CharField(max_length=10, choices=TYPES, null=False, default='tag')
    status = models.IntegerField(max_length=1, choices=settings.CONTENT_STATUS, null=False, default=1)
    network_id = models.ForeignKey(Network, null=True, default=0)
    important = models.BooleanField(default=False)


class Event(models.Model):
<<<<<<< HEAD
	STATUS = ((0, 'Close'), (1, 'Open'), (2, 'Hidden'), (3, 'Draft'))
	
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	status = models.IntegerField(max_length=1, choices=STATUS, null=False, default=0)
	slug = models.CharField(max_length=250)
	created = models.DateTimeField(default=datetime.now(), null=True, blank=True)

	def __unicode__(self):
	   return u'%s (%s)' % (self.name, self.description)
=======
    STATUS = ((0, 'Close'), (1, 'Open'), (2, 'Hidden'), (3, 'Draft'))

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    status = models.IntegerField(max_length=1, choices=STATUS, null=False, default=0)
    slug = models.CharField(max_length=250)
    created = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    properties = models.ManyToManyField(Property, through='PropertyEvent')


class PropertyEvent(models.Model):
    event_id = models.ForeignKey(Event)
    property_id = models.ForeignKey(Property)
    status = models.IntegerField(max_length=1, choices=settings.CONTENT_STATUS, null=False, default=1)
>>>>>>> 76967f5957e2278b329ac3920f2b0afa8106376f
