from django.db import models

class Stop(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()
    name_en = models.CharField(max_length=255)
    name_mm = models.CharField(max_length=255)
    road_en = models.CharField(max_length=255, blank=True, null=True)
    road_mm = models.CharField(max_length=255, blank=True, null=True)
    township_en = models.CharField(max_length=255)
    township_mm = models.CharField(max_length=255)

class Route(models.Model):
    route_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=50)
    color = models.CharField(max_length=6)
    stops = models.ManyToManyField(Stop, related_name='routes')
    shape = models.JSONField()
