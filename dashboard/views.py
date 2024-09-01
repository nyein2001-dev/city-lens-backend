from rest_framework import viewsets
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
    pagination_class = CustomPageNumberPagination  # Optional, if pagination is needed
    filter_backends = (DjangoFilterBackend,)  # Optional, if filtering is needed

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    pagination_class = CustomPageNumberPagination  # Optional, if pagination is needed
    filter_backends = (DjangoFilterBackend,)  # Optional, if filtering is needed

class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GeolocationFilter
