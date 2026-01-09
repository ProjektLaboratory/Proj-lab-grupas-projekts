from app.models.base import db


class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    recipes = db.relationship(
        "Recipe",
        secondary="recipe_ingredient", 
        back_populates="ingredients" 
    )

