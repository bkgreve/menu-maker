# menu-maker
Automatically generate weekly menus and shopping lists

## Summary

The purpose of this program is to automatically generate weekly menus and the corresponding grocery/shopping lists from a user-populated database of recipes. The overall goal is to reduce the amount of time spent planning weekly meals and creating shopping lists.

## Usage

### Installation and Setup

Requires Python 3.6 or greater.

```sh
git clone https://github.com/bkgreve/menu-maker.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Setup Database

This program uses a SQL database for storing and querying recipes. To initialize the database, first specify the SQL database in the `config.ini` file under the variable `SQL_DB`. A sample `config.ini` file can be found in the `examples` directory. A MySQL DB was used during development, but the program should work correctly with a SQLite database.

After specifying the database, run the following to create the tables:

```sh
python menu_maker.py init_db
```

### Adding Recipes to Database

Recipes can be stored in JSON files (a sample `recipes.json` file can be found in the `examples` directory) and loaded directly into the database. To load a new recipe, run the following:

```sh
python menu_maker.py load_recipe --json PATH_TO_JSON_FILE
```

Note that if a recipe with the same name already exists in the database, the new recipe will **not** be loaded.
