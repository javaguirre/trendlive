from datetime import datetime

from django.db import models

# Create your models here.

class Event(models.Model):
	STATUS = ((0, 'Close'), (1, 'Open'), (2, 'Hidden'), (3, 'Draft'))
	
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	status = models.IntegerField(max_length=1, choices=STATUS, null=False, default=0)
	slug = models.CharField(max_length=250)
	created = models.DateTimeField(default=datetime.now(), null=True, blank=True)
