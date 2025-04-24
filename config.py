import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///delivery_bot.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
