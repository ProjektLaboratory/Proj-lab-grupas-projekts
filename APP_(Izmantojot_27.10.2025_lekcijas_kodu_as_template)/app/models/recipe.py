from app.models.base import db


recipe_ingredient = db.Table(
    "recipe_ingredient",
    db.Column(
        "recipe_id",
        db.Integer,
        db.ForeignKey("recipes.id"),
        primary_key=True        
    ),
    db.Column(
        "ingredient_id",
        db.Integer,
        db.ForeignKey("ingredients.id"),
        primary_key=True
    )
)


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.String)
    ingredients = db.relationship(
        "Ingredient",
        secondary=recipe_ingredient,
        back_populates="recipes",
    )
    favourite_recipes = db.relationship(
        "FavouriteRecipe",
        back_populates="recipe"
    )