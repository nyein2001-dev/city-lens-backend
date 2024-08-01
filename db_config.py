import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('postgres://u1f1ppkqdof6rb:p63cc0a4c9d8ba05114ab4eac7f77c30c39ae05a7e1dd2c806485a0df98c51a2a@c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/db062dgbvu3ma4', 'postgresql://geo_user:geo_password@localhost/geovisualization')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
