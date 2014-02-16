from rest_framework import generics, permissions


from .serializers import CoordinateSerializer
from .models import Coordinate


class CoordinateList(generics.ListCreateAPIView):
    model = Coordinate
    serializer_class = CoordinateSerializer
    permission_classes = [
        permissions.AllowAny
    ]
