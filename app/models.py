from app import db
import time

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(100), default="Курьер")
    deliveries = db.Column(db.Integer, default=0)
    money = db.Column(db.Integer, default=0)
    last_delivery = db.Column(db.Float, default=0)
    blocked = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Float, default=time.time)
