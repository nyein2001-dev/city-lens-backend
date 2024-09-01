from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeolocationViewSet, StopViewSet, RouteViewSet

router = DefaultRouter()
router.register(r'geolocations', GeolocationViewSet)
router.register(r'stops', StopViewSet)
router.register(r'routes', RouteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
