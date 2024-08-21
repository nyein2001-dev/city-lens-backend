import os
import django
import json
import datetime
import pytz
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

django.setup()

from dashboard.models import Geolocation

logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

def parse_date(date_str):
    try:
        naive_datetime = datetime.datetime.strptime(date_str, '%B, %d %Y %H:%M:%S')
        timezone = pytz.timezone('UTC')
        return timezone.localize(naive_datetime)
    except ValueError:
        logging.error(f"Date parsing error for date: {date_str}")
        return None

def load_geolocation_data():
    with open('jsondata.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            try:
                published_date = parse_date(item.get('published'))
                added_date = parse_date(item.get('added'))

                Geolocation.objects.create(
                    sector=item.get('sector', '')[:50],
                    topic=item.get('topic', '')[:50],
                    insight=item.get('insight', '')[:500],
                    url=item.get('url', '')[:500],
                    region=item.get('region', '')[:100],
                    country=item.get('country', '')[:100],
                    published=published_date,
                    relevance=int(item.get('relevance', 0) or 0),
                    pestle=item.get('pestle', '')[:50],
                    source=item.get('source', '')[:100],
                    title=item.get('title', '')[:1000],
                    likelihood=int(item.get('likelihood', 0) or 0),
                    intensity=int(item.get('intensity', 0) or 0),
                    added=added_date,
                )
            except Exception as e:
                logging.error(f"Error processing item: {item}. Error: {e}")

if __name__ == '__main__':
    load_geolocation_data()
    print("Data loaded successfully.")
