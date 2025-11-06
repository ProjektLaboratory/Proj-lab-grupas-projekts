from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
klienti_file = os.path.join(BASE_DIR, "database", "klienti.xlsx")
recipe_file = os.path.join(BASE_DIR, "database", "recipe.xlsx")

# Klients
try:
    df_klienti = pd.read_excel(klienti_file)
    user_name = df_klienti['name'].iloc[0] if not df_klienti.empty else None
except Exception as e:
    print(f"Warning: klienti.xlsx could not be read: {e}")
    user_name = None

try:
    df_recipe = pd.read_excel(recipe_file)

    alergeni_unik = [
        "Piens", "Olas", "Zemesrieksti", "Rieksti",
        "Soja", "Kvieši", "Zivs", "Jūras veltes"
    ]

    # Unique values from Excel
    cooking_time = sorted(df_recipe['Laiks'].dropna().unique())
    tips = sorted(df_recipe['Tips'].dropna().unique())        # ēdienreizes tips
    virtuve = sorted(df_recipe['Virtuve'].dropna().unique())  # virtuve

    # Unique products
    produkti = set()
    for cell in df_recipe['Produktu saraksts'].dropna():
        produkti.update([p.strip() for p in str(cell).split(',') if p.strip() != ''])
    produkti = sorted(list(produkti))

except Exception as e:
    raise FileNotFoundError(f"Fails {recipe_file} netika atrasts vai nevar tikt lasīts: {e}")


# Routes
@app.route('/')
def home():
    return render_template('index.html',
                           user_name=user_name,
                           alergeni=alergeni_unik,
                           cooking_time=cooking_time,
                           produkti=produkti,
                           tips=tips,
                           virtuve=virtuve)


@app.route('/filter', methods=['POST'])
def filter_recipes():
    selected_allergens = request.form.getlist('alergeni')
    selected_products = request.form.getlist('produkti')
    selected_time = request.form.get('cooking_time')
    selected_tip = request.form.get('Tips')
    selected_virtuve = request.form.get('Virtuve')

    filtered_df = df_recipe.copy()

    if selected_products:
        filtered_df = filtered_df[
            filtered_df['Produktu saraksts'].apply(
                lambda x: any(p in str(x) for p in selected_products)
            )
        ]

    if selected_time:
        filtered_df = filtered_df[filtered_df['Laiks'] == int(selected_time)]

    if selected_tip:
        filtered_df = filtered_df[filtered_df['tips'] == selected_tip]

    if selected_virtuve:
        filtered_df = filtered_df[filtered_df['virtuve'] == selected_virtuve]

    return render_template('index.html',
                           user_name=user_name,
                           alergeni=alergeni_unik,
                           cooking_time=cooking_time,
                           produkti=produkti,
                           tips=tips,
                           virtuve=virtuve,
                           selected_allergens=selected_allergens,
                           selected_products=selected_products,
                           selected_time=selected_time,
                           selected_tip=selected_tip,
                           selected_virtuve=selected_virtuve,
                           recipes=filtered_df.to_dict('records'))


@app.route('/recipe')
def recipe():
    return render_template('recipe.html', user_name=user_name)


@app.route('/favourites')
def favourites():
    return render_template('favourites.html', user_name=user_name)


@app.route('/mypage')
def mypage():
    return render_template('mypage.html', user_name=user_name)


@app.route('/contact')
def contact():
    return render_template('contact.html', user_name=user_name)


@app.route('/register')
def register():
    return render_template('register.html', user_name=user_name)


# Run
if __name__ == '__main__':
    app.run(debug=True)
