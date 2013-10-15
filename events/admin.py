from django.contrib import admin
from .models import Event, Property


class PropertyInline(admin.TabularInline):
    model = Event.properties.through


class PropertyAdmin(admin.ModelAdmin):
    model = Property
    inlines = [PropertyInline, ]


class EventAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ('name', 'to_slug')
    inlines = [PropertyInline, ]
    
    def to_slug(self, obj):
        return ("/%s" % (obj.slug))
    to_slug.short_description = 'Slug'

admin.site.register(Event, EventAdmin)
admin.site.register(Property, PropertyAdmin)
