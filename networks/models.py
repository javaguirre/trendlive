from django.db import models

# Create your models here.

class Network(models.Model):	
	name = models.CharField(max_length=250)
