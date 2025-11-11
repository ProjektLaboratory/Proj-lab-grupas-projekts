

# https://www.sqlitetutorial.net/sqlite-python/insert/

import sqlite3


def create_tables(conn):
    cur = conn.cursor()


    # Creates nutritional values table
    cur.execute('''
        CREATE TABLE nutritional_values(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            calories INTEGER,
            protein REAL,
            carbs REAL,
            fat REAL
        )
    ''')

    # Creates recipes cooking time table
    cur.execute('''
        CREATE TABLE time (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            length INTEGER
        )
    ''')

    # Creates recipes category table
    cur.execute('''
        CREATE TABLE category(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')

    # Create recipes cruisine table
    cur.execute('''
        CREATE TABLE cuisine(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')

    # Creates ingredients table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            nutritional_values_id INTEGER,
            FOREIGN KEY (nutritional_values_id) REFERENCES nutritional_values(id)
        )
    ''')


    # Creates recipes ingriedient table
    cur.execute('''
        CREATE TABLE recipe_ingredients (
            id INTEGER,
            ingredient_id INTEGER,
            measurement TEXT,
            PRIMARY KEY (id, ingredient_id),
            FOREIGN KEY (recipe_id) REFERENCES recipes(id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
        )
    ''')

    # Creates recipes table
    cur.execute('''
        CREATE TABLE recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            recipe_ingredients_id INTEGER,
            time_id INTEGER,
            category_id INTEGER,
            cuisine_id INTEGER,
            FOREIGN KEY (recipe_ingredients_id) REFERENCES recipe_ingredients(id),
            FOREIGN KEY (time_id) REFERENCES time(id),
            FOREIGN KEY (category_id) REFERENCES category(id),
            FOREIGN KEY (cuisine_id) REFERENCES cuisine(id)
        )
    ''')

    # Creates favourite_recipes table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS favourite_recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            favourites TEXT,
            FOREIGN KEY (favourites) REFERENCES recipes (name)
        )
    ''')

    # Creates users table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surnname TEXT,
            email TEXT,
            favourite_recipes_id INTEGER,
            FOREIGN KEY (favourite_recipes_id) REFERENCES favourite_recipes (id)
        )
    ''')

    conn.commit()



def add_recipe(conn, recipe):
    # insert table statement
    sql = ''' INSERT INTO recipes(name, instructions, ingredients)
              VALUES (?, ?, ?) '''

    # Create  a cursor
    cur = conn.cursor()

    # execute the INSERT statement
    cur.execute(sql, recipe)

    # commit the changes
    conn.commit()

    # get the id of the last inserted row
    return cur.lastrowid


def add_favourite_recipe(conn, favourite_recipe):
    # insert table statement
    sql = '''INSERT INTO favourite_recipes(title, recipes)
             VALUES (?, ?) '''

    # create a cursor
    cur = conn.cursor()

    # execute the INSERT statement
    cur.execute(sql, favourite_recipe)

    # commit the changes
    conn.commit()

    # get the id of the last inserted row
    return cur.lastrowid


def main():
    try:
        with sqlite3.connect('app.db') as conn:
            create_tables(conn)
            # add  a project
            recipe = ('test_recipe_a+b', 'apvienot a un b', 'a, b')
            recipe_id = add_recipe(conn, recipe)
            print(f'Created a recipe with the id {recipe_id}')

            # add tasks to the project
            favourite_recipes = [
                ('test_a_favourite', recipe_id),
                ('test_other_favourite', recipe_id)
            ]

            for favourite_recipe in favourite_recipes:
                favourite_recipe_id = add_favourite_recipe(conn, favourite_recipe)
                print(f'Created favourite recipe with the id {favourite_recipe_id}')


    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    main()