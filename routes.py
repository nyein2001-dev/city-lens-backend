from flask import Flask, jsonify
from app import app, db
from models.geolocation import Geolocation
import re
from datetime import datetime

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

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
