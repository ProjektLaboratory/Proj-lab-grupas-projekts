from os import access

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.testing.pickleable import Order

from .. import db
from ..models import Recipe

access_bp = Blueprint("access", __name__, url_prefix="/access")


@access_bp.get("/")
def index():
    """
    q = request.args.get("q") or "").stip()
    query = Order.query
    if q:
        like = f"%{q}%"
        quary = query.filter((Recipe.ingredients.ilike(like)))
    orders = query.order_by(Recipe.name.asc()).all()
    """
    return render_template("register-and-login/access.html")

@access_bp.get("/new")
def new():
    return render_template("register-and-login/new.html")