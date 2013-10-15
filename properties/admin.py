from django.contrib import admin
from events.models import Event
from networks.models import Network

from .models import Property

class PropertyAdmin(admin.ModelAdmin):
	search_fields = ("value",)
	list_display = ('value','type')
	
admin.site.register(Property,PropertyAdmin)