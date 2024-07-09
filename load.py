import json
from app import app, db  # Import the Flask app and db instance
from models import Geolocation

def truncate_string(value, max_length):
    if value and len(value) > max_length:
        return value[:max_length]
    return value

# Load JSON data
with open('jsondata.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create an application context
with app.app_context():
    # Process each item from JSON data and add to the database
    for item in data:
        # Handle integer fields
        relevance = int(item['relevance']) if item['relevance'] != "" else None
        likelihood = int(item['likelihood']) if item['likelihood'] != "" else None
        intensity = int(item['intensity']) if item['intensity'] != "" else None

        # Handle date fields
        published = item['published'] if item['published'] != "" else None
        added = item['added'] if item['added'] != "" else None

        # Truncate string fields to a maximum length of 100 characters
        sector = truncate_string(item.get('sector'), 50)
        topic = truncate_string(item.get('topic'), 50)
        insight = truncate_string(item.get('insight'), 500)
        url = truncate_string(item.get('url'), 500)
        region = truncate_string(item.get('region'), 100)
        country = truncate_string(item.get('country'), 100)
        pestle = truncate_string(item.get('pestle'), 50)
        source = truncate_string(item.get('source'), 100)
        title = truncate_string(item.get('title'), 1000)

        # Create Geolocation object
        geolocation = Geolocation(
            sector=sector,
            topic=topic,
            insight=insight,
            url=url,
            region=region,
            country=country,
            published=published,
            relevance=relevance,
            pestle=pestle,
            source=source,
            title=title,
            likelihood=likelihood,
            intensity=intensity,
            added=added
        )
        db.session.add(geolocation)

    # Commit changes to the database
    db.session.commit()
