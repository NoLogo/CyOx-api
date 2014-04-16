import datetime

from django.db import models
from pygeocoder import Geocoder
# from mapping import create_route


class Coordinate(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    convert = models.BooleanField(default=False)
    request_made = models.TimeField()

    class Meta:
        ordering = ['request_made']

    def save(self, *args, **kwargs):
        if self.convert:
            start = Geocoder.geocode(self.start_point)
            lat = start.latitude
            lng = start.longitude
            self.start_point = repr(lat) + ',' + repr(lng)

            self.convert = False
        end = Geocoder.geocode(self.end_point)
        lat = end.latitude
        lng = end.longitude
        self.end_point = repr(lat) + ',' + repr(lng)
        self.request_made = datetime.datetime.now()
        return super(Coordinate, self).save(*args, **kwargs)
