from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def init_app(app, **kwargs):
    db.init_app(app)

class Rectangle(db.Model):

    __tablename__ = 'rectangle'

    def __init__(self, length, width):
        self.length = length
        self.width = width


    id = db.Column(db.Integer, primary_key=True)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "length": self.length,
            "width": self.width
        }


class Square(db.Model):

    __tablename__ = 'square'

    def __init__(self, side):
        self.side = side

    id = db.Column(db.Integer, primary_key=True)
    side = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "side": self.side
        }

class Triangle(db.Model):

    __tablename__ = 'triangle'

    def __init__(self, side_a, side_c, base, height):
        self.side_a = side_a
        self.side_c = side_c
        self.base = base
        self.height = height

    id = db.Column(db.Integer, primary_key=True)
    side_a = db.Column(db.Float)
    side_c = db.Column(db.Float)
    base = db.Column(db.Float)
    height = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "side_a": self.side_a,
            "side_c": self.side_c,
            "base": self.base,
            "height": self.height
        }
