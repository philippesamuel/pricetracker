from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Market(db.Model):
    """Market model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    adress = db.Column(db.String(240), unique=False, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name!r}>'

    def __str__(self):
        return repr(self.name)


class Product(db.Model):
    """Product model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name!r}>'

    def __str__(self):
        return repr(self.name)


class Price(db.Model):
    """Price model."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('prices', lazy=True))
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'), nullable=False)
    market = db.relationship('Market', backref=db.backref('prices', lazy=True))
    date_time = db.Column(db.DateTime, unique=False, nullable=False)
    unit_price = db.Column(db.Integer, unique=False, nullable=False)
    unit = db.Column(db.String(40), unique=False, nullable=False)
    quantity_per_unit = db.Column(db.Float, unique=False, nullable=True)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.product!s}: {self.unit_price}>'

