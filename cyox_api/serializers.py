from rest_framework import serializers

from .models import Coordinate


class CoordinateSerializer(serializers.ModelSerializer):
    coordinate = serializers.HyperlinkedIdentityField('coordinate', view_name='coordinate-list')

    class Meta:
        model = Coordinate
        fields = ('start_point', 'end_point', 'convert')
