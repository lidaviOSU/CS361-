from application import db


class MSDS(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    cas = db.Column(db.String(length=50), nullable=False)
    internal = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    user = db.Column(db.String(length=50), nullable=False)
    vendor = db.Column(db.String(length=50),nullable=False)
    comments = db.Column(db.String(length=500), nullable=True)


class hazard(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    assessment = db.Column(db.String(length=50), nullable=False)
    internal = db.Column(db.Integer(), nullable=False, unique=True)
    year = db.Column(db.Integer(), nullable=False)
    user = db.Column(db.String(length=50), nullable=False)
    comments = db.Column(db.String(length=250),nullable=False)
