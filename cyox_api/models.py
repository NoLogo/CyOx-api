import datetime

from django.db import models
from postcodes import PostCoder
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
            lat = self.start_point.split()[0]
            lng = self.start_point.split()[1]
            postcode = PostCoder().get_nearest(lat, lng)
            self.start_point = postcode['postcode']
            self.convert = False
        self.request_made = datetime.datetime.now()
        return super(Coordinate, self).save(*args, **kwargs)
