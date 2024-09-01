from django.db import models

class Geolocation(models.Model):
    sector = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    insight = models.TextField(max_length=500, blank=True)
    url = models.URLField(max_length=500, blank=True)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    published = models.DateTimeField(null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    likelihood = models.IntegerField(null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    added = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

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
