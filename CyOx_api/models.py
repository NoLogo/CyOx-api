import datetime

from django.db import models


class Coordinate(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    request_made = models.TimeField()

    class Meta:
        ordering = ['request_made']

    def save(self, *args, **kwargs):
        self.request_made = datetime.datetime.now()
        return super(Coordinate, self).save(*args, **kwargs)
