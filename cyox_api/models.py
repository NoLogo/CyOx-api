import datetime

from django.db import models


class Coordinate(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    request_made = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-request_made']
