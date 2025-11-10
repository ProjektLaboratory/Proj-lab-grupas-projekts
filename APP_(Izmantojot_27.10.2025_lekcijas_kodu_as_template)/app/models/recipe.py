from app.models.base import db


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.String)
    ingredients = db.relationship(
        "Ingredient",
        back_populates="recipes",
    )
    favorites = db.relationship(
        "FavoriteRecipe",
        back_populates="recipes",
    )
