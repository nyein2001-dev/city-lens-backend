from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Geolocation
from .serializers import GeolocationSerializer
from .pagination import CustomPageNumberPagination
from .filters import GeolocationFilter

class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GeolocationFilter
