import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
django.setup()

import csv
import json
import glob
from django.core.management.base import BaseCommand
from django.db import transaction
from dashboard.models import Stop, Route

class Command(BaseCommand):
    help = 'Import data from TSV files to the database'

    def handle(self, *args, **kwargs):
        self.import_stops()
        self.import_routes()

    @transaction.atomic
    def import_stops(self):
        tsv_path = 'data/stops.tsv'
        with open(tsv_path, mode='r', encoding='utf-8') as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter='\t')
            for row in reader:
                stop_data = {
                    'lat': float(row['lat']),
                    'lng': float(row['lng']),
                    'name_en': row['name_en'],
                    'name_mm': row['name_mm'],
                    'road_en': row.get('road_en', ''),
                    'road_mm': row.get('road_mm', ''),
                    'township_en': row['township_en'],
                    'township_mm': row['township_mm']
                }
                Stop.objects.update_or_create(id=int(row['id']), defaults=stop_data)
        self.stdout.write(self.style.SUCCESS('Successfully imported stops'))

    @transaction.atomic
    def import_routes(self):
        json_pattern = 'data/routes/*.json'
        for path in glob.glob(json_pattern):
            with open(path, 'r', encoding='utf-8') as jsonfile:
                route_data = json.load(jsonfile)
                agency_id = route_data.get('agency_id', None)
                if not agency_id:
                    continue
                route, _ = Route.objects.update_or_create(
                    route_id=route_data['route_id'],
                    defaults={
                        'name': route_data['name'],
                        'agency_id': agency_id,
                        'color': route_data.get('color', ''),
                        'shape': route_data.get('shape', {})
                    }
                )
                stops = Stop.objects.filter(id__in=route_data.get('stops', []))
                route.stops.set(stops)
        self.stdout.write(self.style.SUCCESS('Successfully imported routes'))

if __name__ == "__main__":
    Command().handle()
