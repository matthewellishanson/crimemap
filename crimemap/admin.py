from django.contrib import admin

from crimemap.models import Incidentcode, Status, Building, Location, Incident

class LocationInline(admin.TabularInline):
    model = Location

class BuildingAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [
        LocationInline,
    ]

admin.site.register(Incidentcode)
admin.site.register(Status)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Location)
admin.site.register(Incident)
