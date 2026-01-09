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
    time = db.Column(db.String(50))
    cuisine = db.Column(db.String(50))
    meal_type = db.Column(db.String(50))
    allergens = db.Column(db.String(200))
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
    nutrients = db.relationship(
        "NutritionalValues",
        back_populates="recipe",
        uselist=False
    )