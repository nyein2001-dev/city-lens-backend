import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from db_config import Config
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

from routes import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)