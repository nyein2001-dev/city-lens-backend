import django_filters
from django.db.models import Q
from .models import Geolocation

class GeolocationFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Geolocation
        fields = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(sector__icontains=value) |
            Q(topic__icontains=value) |
            Q(insight__icontains=value) |
            Q(region__icontains=value) |
            Q(country__icontains=value) |
            Q(pestle__icontains=value) |
            Q(source__icontains=value)
        )