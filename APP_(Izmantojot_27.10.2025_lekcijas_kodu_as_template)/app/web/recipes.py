from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.testing.pickleable import Order

from .. import db
from ..models import Recipe

from flask_login import current_user


recipes_bp = Blueprint("recipes", __name__, url_prefix="/recipes")


@recipes_bp.route("/", methods=["GET"])
def index():
    allergen = request.args.get("allergen", "")
    product = request.args.get("product", "")
    time = request.args.get("time", "")
    cuisine = request.args.get("cuisine", "")
    meal_type = request.args.get("meal_type", "")

    query = Recipe.query

    if allergen:
        query = query.filter(Recipe.allergens.ilike(f"%{allergen}%"))

    if product:
        query = query.join(Recipe.ingredients).filter(
            Ingredient.name.ilike(f"%{product}%")
        )

    if time:
        query = query.filter(Recipe.time.ilike(f"%{time}%"))

    if cuisine:
        query = query.filter(Recipe.cuisine.ilike(f"%{cuisine}%"))

    if meal_type:
        query = query.filter(Recipe.meal_type.ilike(f"%{meal_type}%"))

    recipes = query.all()

    return render_template(
        "recipes/recipe.html",
        recipes=recipes,
        allergen=allergen,
        product=product,
        time=time,
        cuisine=cuisine,
        meal_type=meal_type
    )

@recipes_bp.get("/new")
def new():
    return render_template("recipes/new.html")