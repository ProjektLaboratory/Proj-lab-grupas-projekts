from app.models.base import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    favorites = db.relationship(
        "FavoriteRecipe",
        back_populates="recipes",
    )