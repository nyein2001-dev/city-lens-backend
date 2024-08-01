import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

from models.geolocation import Geolocation
from routes import *

with app.app_context():
    db.create_all()

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

if __name__ == '__main__':
    app.run(debug=True)
