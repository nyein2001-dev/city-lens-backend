from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeolocationViewSet

router = DefaultRouter()
router.register(r'geolocations', GeolocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
