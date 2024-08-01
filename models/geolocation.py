from app import db

class Geolocation(db.Model):
    __tablename__ = 'geolocation'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(50))
    topic = db.Column(db.String(50))
    insight = db.Column(db.String(500))
    url = db.Column(db.String(500))
    region = db.Column(db.String(100))
    country = db.Column(db.String(100))
    published = db.Column(db.DateTime)
    relevance = db.Column(db.Integer)
    pestle = db.Column(db.String(50))
    source = db.Column(db.String(100))
    title = db.Column(db.String(1000))
    likelihood = db.Column(db.Integer)
    intensity = db.Column(db.Integer)
    added = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Geolocation {self.id}>'
