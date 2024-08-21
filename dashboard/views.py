from rest_framework import viewsets
from .custom_page_number_pagination import CustomPageNumberPagination
from .models import Geolocation
from .serializers import GeolocationSerializer

class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    pagination_class = CustomPageNumberPagination