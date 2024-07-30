from flask import Flask, jsonify
from app import app, db
from models.geolocation import Geolocation

@app.route('/getAllGeoLocationData', methods=['GET'])
def get_geolocations():
    geolocations = Geolocation.query.all()
    data = [
        {
            'id': geo.id,
            'sector': geo.sector,
            'topic': geo.topic,
            'insight': geo.insight,
            'url': geo.url,
            'region': geo.region,
            'country': geo.country,
            'published': geo.published,
            'relevance': geo.relevance,
            'pestle': geo.pestle,
            'source': geo.source,
            'title': geo.title,
            'likelihood': geo.likelihood,
            'intensity': geo.intensity,
            'added': geo.added
        }
        for geo in geolocations
    ]
    return jsonify(data)
