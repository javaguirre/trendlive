from django.contrib import admin
from .models import Network

class NetworkAdmin(admin.ModelAdmin):
	search_fields = ("name",)
	
admin.site.register(Network, NetworkAdmin)
