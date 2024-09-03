from rest_framework import viewsets, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .models import Geolocation
from .serializers import GeolocationSerializer
from .pagination import CustomPageNumberPagination
from .filters import GeolocationFilter
from .models import Stop, Route
from .serializers import StopSerializer, RouteSerializer

class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)

class RouteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'route_id', 'name', 'agency_id', 'color']

class RouteDetailSerializer(serializers.ModelSerializer):
    stops = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Route
        fields = ['shape', 'stops']

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action == 'list':
            return RouteListSerializer
        if self.action == 'retrieve':
            return RouteDetailSerializer
        return RouteSerializer


class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GeolocationFilter
