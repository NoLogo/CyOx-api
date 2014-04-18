from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .serializers import CoordinateSerializer
from .models import Coordinate
from .mapping import get_route


class CoordinateList(ListCreateAPIView):
    model = Coordinate
    permission_classes = [AllowAny]
    serializer_class = CoordinateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA, files=request.FILES)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            route = get_route(self.object.start_point, self.object.end_point)
            return Response(route, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
