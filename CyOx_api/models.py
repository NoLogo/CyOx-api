from django.db import models


class Coordinates(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    request_made = models.TimeField()

    class Meta:
        ordering = ['request_made']
