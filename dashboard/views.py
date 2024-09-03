from rest_framework import viewsets, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .models import Geolocation, Stop, Route
from .serializers import GeolocationSerializer, StopSerializer, RouteSerializer
from .pagination import CustomPageNumberPagination
from .filters import GeolocationFilter

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
    stops = StopSerializer(many=True, read_only=True)  # Use StopSerializer here

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
