from flask import Blueprint, render_template, request, redirect, url_for
from ..models import FavouriteRecipe

favourite_recipes_bp = Blueprint("favourite-recipes", __name__, url_prefix="/favourites")


@favourite_recipes_bp.get("/")
def index():
    """
    q = request.args.get("q") or "").stip()
    query = Order.query
    if q:
        like = f"%{q}%"
        quary = query.filter((FavouriteRecipe.title.ilike(like)))
    orders = query.order_by(Recipe.id.asc()).all()
    """
    #return render_template("favourite-recipes/favourites.html")
    return render_template("favourite-recipes/favourites.html")
