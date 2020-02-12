from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Area_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    population = db.Column(db.String(120))
    longitude = db.Column(db.String(120))
    latitude = db.Column(db.String(120))
    zipcode = db.Column(db.String(120))

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }