from django.contrib import admin
from .models import Coordinate


class CoordinateAdmin(admin.ModelAdmin):
    list_display = ['start_point', 'end_point', 'request_made']

admin.site.register(Coordinate, CoordinateAdmin)
