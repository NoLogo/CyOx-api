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
            self.start_point = self.start_point + ', Oxford'
            start = Geocoder.geocode(self.start_point)
            lat = start.latitude
            lng = start.longitude
            self.start_point = repr(lng) + ',' + repr(lat)

            self.convert = False
        self.end_point = self.end_point + ', Oxford'
        end = Geocoder.geocode(self.end_point)
        lat = end.latitude
        lng = end.longitude
        self.end_point = repr(lng) + ',' + repr(lat)
        self.request_made = datetime.datetime.now()
        return super(Coordinate, self).save(*args, **kwargs)
