from app.models.base import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    favourites = db.relationship(
        "FavouriteRecipe",
        #back_populates="recipes",
        back_populates="user"
    )