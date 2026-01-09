from app.models.base import db


class NutritionalValues(db.Model):
    __tablename__ = "Nutritional_values"
    id = db.Column(db.Integer, primary_key=True)
    kalorijas = db.Column(db.Integer)
    olbaltumvielas = db.Column(db.String)
    tauki = db.Column(db.String)
    oglhidrati = db.Column(db.String)
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey("recipes.id"),
        unique=True
    )
    recipe = db.relationship(
        "Recipe",
        back_populates="nutrients"
    )
