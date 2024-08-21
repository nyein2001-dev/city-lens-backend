from rest_framework import viewsets
from .models import Geolocation
from .serializers import GeolocationSerializer

class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
