import decimal

from rest_framework import serializers
from pygeocoder import Geocoder

from .models import Coordinate


def clean_geodata(point):
    bits = point.split(',')
    lat = None
    lng = None
    if len(bits) == 2:
        try:
            lat = decimal.Decimal(bits[0])
            lng = decimal.Decimal(bits[1])
        except decimal.InvalidOperation:
            pass
    if lng is None or lat is None:
        start = Geocoder.geocode(point + ', Oxfordshire')
        lat = start.latitude
        lng = start.longitude
    return str(lat) + ',' + str(lng)


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ('start_point', 'end_point', 'request_made')
        read_only_fields = ('request_made',)

    def validate_start_point(self, attrs, source):
        attrs[source] = clean_geodata(attrs.get(source))
        return attrs

    def validate_end_point(self, attrs, source):
        attrs[source] = clean_geodata(attrs.get(source))
        return attrs
