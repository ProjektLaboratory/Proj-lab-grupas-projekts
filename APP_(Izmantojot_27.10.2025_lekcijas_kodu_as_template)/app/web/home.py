from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.testing.pickleable import Order

from .. import db
from ..models import Recipe

home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.get("/")
def index():
    """
    q = request.args.get("q") or "").stip()
    query = Order.query
    if q:
        like = f"%{q}%"
        quary = query.filter((Recipe.ingredients.ilike(like)))
    orders = query.order_by(Recipe.name.asc()).all()
    """
    return render_template("home.html")