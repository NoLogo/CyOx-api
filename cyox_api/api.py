from rest_framework.generics import ListCreateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from .serializers import CoordinateSerializer
from .models import Coordinate
from .mapping import get_route


class CoordinateList(ListCreateAPIView):
    model = Coordinate
    permission_classes = [AllowAny]
    renderer_classes = (JSONRenderer,)
    serializer_class = CoordinateSerializer

    # def create(self, request, *args, **kwargs):
    #     response = super(CoordinateList, self).create(request, *args, **kwargs)
    #     route = get_route(response.data['start_point'], response.data['end_point'])
    #     print route
    #     print dir(route)
    #     return response, Response(route)
