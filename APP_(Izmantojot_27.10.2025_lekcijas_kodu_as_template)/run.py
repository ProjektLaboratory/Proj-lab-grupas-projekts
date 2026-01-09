from app.models import recipe, ingredient, favourite_recipe, user
from app.models.adds_data_app_db import load_data_from_excel
from app import create_app, db
from flask_migrate import Migrate


app = create_app()
migrate = Migrate(app, db)  # enables Alembic via Flask-Migrate

if __name__ == "__main__":
    
    with app.app_context():
        print("DB URI:", app.config['SQLALCHEMY_DATABASE_URI'])
        db.create_all()
        print("Tables:", db.metadata.tables.keys())
    #app.run(debug=True)
    load_data_from_excel()
    app.run(host='0.0.0.0', port=26019, debug=True)
