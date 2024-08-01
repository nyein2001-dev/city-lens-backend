import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('postgresql://u1f1ppkqdof6rb:p63cc0a4c9d8ba05114ab4eac7f77c30c39ae05a7e1dd2c806485a0df98c51a2a@c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/db062dgbvu3ma4')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


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
