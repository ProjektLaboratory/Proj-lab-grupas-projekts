from app.models.base import db


class FavouriteRecipe(db.Model):
    __tablename__ = "favourite_recipes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    recipes = db.relationship(
        "Recipe",
        back_populates="favourite_recipes",
    )
