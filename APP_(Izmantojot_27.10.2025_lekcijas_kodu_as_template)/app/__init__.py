from flask import Flask, render_template

#from .models import Author, Book, Order
#from .models import Ingredient, Recipe, FavouriteRecipe
#from .models import Recipe, FavouriteRecipe
from .models.base import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register web blueprints (split by entity)
    """
    from .web.authors import authors_bp
    from .web.books import books_bp
    from .web.orders import orders_bp
    app.register_blueprint(authors_bp)  # /authors
    app.register_blueprint(books_bp)  # /books
    app.register_blueprint(orders_bp)  # /orders
    """
    from .web.access import access_bp
    from .web.recipes import recipes_bp
    from .web.favourite_recipes import favourite_recipes_bp
    from .web.contact import contact_bp
    from .web.my_page import my_page_bp
    app.register_blueprint(access_bp) # /access
    app.register_blueprint(recipes_bp)  # /recipes
    app.register_blueprint(favourite_recipes_bp)  # /favourite_recipes
    app.register_blueprint(contact_bp) # /contact_info
    app.register_blueprint(my_page_bp) # /my_page

    # Register api endpoints
    from .api import api_bp
    app.register_blueprint(api_bp)

    @app.get("/")
    def home():
        return render_template(
            "home.html",
            #'register-and-login/access.html',

            #author_count=Author.query.count(),
            #book_count=Book.query.count(),
            #order_count=Order.query.count(),

            #ngredient_count=Ingredient.query.count(),
            #recipe_count=Recipe.query.count(),
            #favourite_recipe_count=FavouriteRecipe.query.count(),
        )

    return app
