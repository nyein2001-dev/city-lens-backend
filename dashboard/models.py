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
