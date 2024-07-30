import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://geo_user:geo_password@localhost/geovisualization')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
