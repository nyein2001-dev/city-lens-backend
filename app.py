from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

# Import routes after creating `db` to avoid circular import
from routes import *

# Create all tables inside the application context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
