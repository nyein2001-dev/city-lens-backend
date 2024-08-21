from django.contrib import admin
from django.urls import path, include
from .views import ping
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger UI
schema_view = get_schema_view(
   openapi.Info(
      title="City Lens API Documentation",
      default_version='v1',
      description="API documentation for City Lens",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"),
    path('api/items/', include('items.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]