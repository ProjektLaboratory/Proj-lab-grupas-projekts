import os
import sys
import pandas as pd
from app import create_app
from app.models.base import db
from app.models.recipe import Recipe
from app.models.ingredient import Ingredient
from app.models.nutritional_value import NutritionalValues

app = create_app()

def load_data_from_excel():
    #database_path='C:/Project-Limpa/Proj-lab-grupas-projekts/APP_(Izmantojot_27.10.2025_lekcijas_kodu_as_template)/app.db'
    #if os.path.exists(database_path):
    #    os.remove(database_path)
    #    print(f"{database_path} sql datubāzes fails tiek izdzēsts, lai to izveidotu jauno versiju")
    #else:
    #    print("Sql datubāzes fails neeksistē.")
            
    with app.app_context():
        sys.stdout.reconfigure(encoding='utf-8')
        db.drop_all()
        db.create_all()
        
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
            #raw = row.get('Recepte', '') 
            #if pd.isna(raw):
            #    raw = ''
            #pagatavosana = str(raw).strip().replace('\r', '').replace('\n', '<br>')
            if exists:
                #exists.instructions=pagatavosana
                continue
            
            ALERGENU_KARTES = {
                'Piens': 'piens',
                'Olas': 'olas',
                'Zemessriekti': 'zemesrieksti',
                'Rieksti': 'rieksti',
                'Soja': 'soja',
                'Kvieši': 'kvieši',
                'Zivs': 'zivs',
                'Jūras veltes': 'jūras veltes'
            }
            alergeni = []
            for kolonna, nosaukums in ALERGENU_KARTES.items():
                if str(row.get(kolonna, '0')).strip() == '1':
                    alergeni.append(nosaukums)
            alergeni_str = ", ".join(alergeni)
            
            recipe = Recipe(
                name=row['Nosaukums'],
                instructions=(str(row.get('Recepte', '')).strip()).replace('\r', '').replace('\n', '<br>'),
                meal_type=row.get('Tips', ''),
                time=row.get('Laiks', ''),
                cuisine=row.get('Virtuve', ''),
                allergens=alergeni_str,
                #kalorijas=row.get('Kalorijas', None),
                #olbaltumvielas=str(row.get('Olbaltumvielas', '')).strip(),
                #tauki=str(row.get('Tauki', '')).strip(),
                #oglhidrati=str(row.get('Ogļhidrāti', '')).strip()
            )
            
            recipe.nutrients = NutritionalValues(
                kalorijas=row.get('Kalorijas', None),
                olbaltumvielas=str(row.get('Olbaltumvielas', '')).strip(),
                tauki=str(row.get('Tauki', '')).strip(),
                oglhidrati=str(row.get('Ogļhidrāti', '')).strip()
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

        print(df_recipes.columns.tolist())

if __name__ == "__main__":
    load_data_from_excel()