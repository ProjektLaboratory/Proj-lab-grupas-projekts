import os
import sys
import pandas as pd
from app import create_app
from app.models.base import db
from app.models.recipe import Recipe
from app.models.ingredient import Ingredient

app = create_app()

def load_data_from_excel():
    with app.app_context():
        sys.stdout.reconfigure(encoding='utf-8')
        #df_produkti = pd.read_excel('produkti.xlsx')
        #df_recipes = pd.read_excel('recipe.xlsx')
        BASE_DIR = os.path.dirname(__file__) 
        df_produkti = pd.read_excel(os.path.join(BASE_DIR, 'produkti.xlsx')) 
        df_recipes = pd.read_excel(os.path.join(BASE_DIR, 'recipe.xlsx'))
        #print(df_produkti.columns.tolist())
        #print(df_recipes.columns.tolist())
        
        for _, row in df_produkti.iterrows():
            exists = Ingredient.query.filter_by(name=row['Produktu saraksts:']).first()
            if not exists:
                jauns_ing = Ingredient(name=row['Produktu saraksts:'])
                db.session.add(jauns_ing)
        db.session.commit()
        
        
        for _, row in df_recipes.iterrows():
            exists = Recipe.query.filter_by(name=row['Nosaukums']).first()
            if exists:
                continue

            recipe = Recipe(
                name=row['Nosaukums'],
                instructions=row.get('Instrukcija', 'Nav instrukcijas'),
                meal_type=row.get('Tips', ''),
                time=row.get('Laiks', ''),
                cuisine=row.get('Virtuve', ''),
                allergens=row.get('Alergēni', '')
            )

            db.session.add(recipe)
            db.session.flush()

            raw_products = row.get('Produkti', '')
            if isinstance(raw_products, str):
                ingredient_names = [p.strip() for p in raw_products.split(',') if p.strip()]
                for ing_name in ingredient_names:
                    ing = Ingredient.query.filter_by(name=ing_name).first()
                    if ing:
                        recipe.ingredients.append(ing)

        try:
            db.session.commit()
            print("Visi dati no Excel veiksmīgi ielādēti!")
        except Exception as e:
            db.session.rollback()
            print(f"Kļūda saglabājot datus: {e}")



if __name__ == "__main__":
    load_data_from_excel()