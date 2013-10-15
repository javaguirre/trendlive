from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ('name', 'to_slug')
    
    def to_slug(self, obj):
        return ("/%s" % (obj.slug))
    to_slug.short_description = 'Slug'
	
admin.site.register(Event,EventAdmin)
