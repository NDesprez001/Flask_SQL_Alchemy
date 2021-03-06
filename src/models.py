from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(120))
    # image = db.Column(db.String(10000))

    jobs = db.relationship('Jobs', back_populates='user')

    def __repr__(self):
        return '<Users %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "jobs": [x.serialize() for x in self.jobs]
        }

class Area_info(db.Model):
    __tablename__='area_info'
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

class Jobs(db.Model):
    __tablename__='jobs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    job_name = db.Column(db.String(120))
    job_place = db.Column(db.String(120))
    job_pay = db.Column(db.String(120))

    user = db.relationship('Users', back_populates='jobs')

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "job_name": self.job_name,
            "job_place": self.job_place,
            "job_pay": self.job_pay,
        }