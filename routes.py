from flask import render_template
from app import app, db
from models import Geolocation  # Import specific model here

@app.route('/')
def index():
    geolocations = Geolocation.query.all()
    return render_template('index.html', geolocations=geolocations)
