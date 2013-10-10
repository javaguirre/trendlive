from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
	search_fields = ("name",)
	
admin.site.register(Event,EventAdmin)