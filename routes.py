from flask import Flask, jsonify
from app import app, db
from models import Geolocation  # Import specific model here

# @app.route('/')
# def index():
#     geolocations = Geolocation.query.all()
#     return render_template('index.html', geolocations=geolocations)

@app.route('/', methods=['GET'])
def get_geolocations():
    geolocations = Geolocation.query.all()
    data = [
        {
            'id': geo.id,
            'topic': geo.topic,
            'insight': geo.insight,
            'country': geo.country,
            'title': geo.title
        }
        for geo in geolocations
    ]
    return jsonify(data)
