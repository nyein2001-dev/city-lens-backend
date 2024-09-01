from django.db import models
from dashboard.bus_stop_model import Stop


class Route(models.Model):
    route_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=50)
    color = models.CharField(max_length=6)
    stops = models.ManyToManyField(Stop, related_name='routes')
    shape = models.JSONField()
