import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or "mysql+mysqlconnector://root:admin@localhost:3306/wishlist_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
