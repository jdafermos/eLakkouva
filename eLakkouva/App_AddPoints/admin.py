from django.contrib import admin
from .models import Pits, Bulbs, Leaks
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class PitsAdmin(LeafletGeoAdmin):
    list_display = ('Comment', 'Coords')
admin.site.register(Pits, PitsAdmin)

class BulbsAdmin(LeafletGeoAdmin):
    list_display = ('Comment', 'Coords')
admin.site.register(Bulbs, BulbsAdmin)

class LeaksAdmin(LeafletGeoAdmin):
    list_display = ('Comment', 'Coords')
admin.site.register(Leaks, LeaksAdmin)