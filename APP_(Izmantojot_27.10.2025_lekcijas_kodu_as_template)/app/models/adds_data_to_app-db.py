

# https://www.sqlitetutorial.net/sqlite-python/insert/

import sqlite3


def create_tables(conn):
    cur = conn.cursor()

    # Create recipes table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            instructions TEXT,
            ingredients TEXT
        )
    ''')

    # Create favourite_recipes table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS favourite_recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            recipes INTEGER,
            FOREIGN KEY (recipes) REFERENCES recipes (id)
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