from rest_framework import serializers
from .models import Geolocation
from .models import Stop, Route

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context.get('request')
        if request and request.method == 'GET':
            if request.parser_context['kwargs'].get('pk'):
                self.fields = {
                    'shape': serializers.JSONField(),
                    'stops': StopSerializer(many=True, read_only=True)
                }
            else:
                self.fields = {
                    'id': serializers.IntegerField(),
                    'route_id': serializers.CharField(),
                    'name': serializers.CharField(),
                    'agency_id': serializers.CharField(),
                    'color': serializers.CharField(),
                }
        return super(RouteSerializer, self).to_representation(instance)

class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = '__all__'