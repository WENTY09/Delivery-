import os

class Config:
    # Строка подключения к PostgreSQL из Render
    SQLALCHEMY_DATABASE_URI = os.getenv("postgresql://wenty:4tf4gCkox2X0TbrluhFYo522s2BrP44J@dpg-d05b9lruibrs73fi0cm0-a/delivery_bot")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("UvWO2pXY2409JZFIH4GVdKYqgzDpwtn6", "UvWO2pXY2409JZFIH4GVdKYqgzDpwtn6")
