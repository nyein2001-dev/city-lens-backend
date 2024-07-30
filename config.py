import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://geo_user:geo_password@localhost/geovisualization'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
