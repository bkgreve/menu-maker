import configparser

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modules.add_recipe import add_new_recipe
from database.meal_maker_db import Recipe, Ingredient, RecipeIngredient, Base

config = configparser.ConfigParser()
config.read('config.ini')
SQL_DB = config['DEFAULT']['SQL_DB']


@click.group()
def cli():
    """Menu Maker: Creates Menus and Grocery Lists"""
    pass


@cli.command('load_recipe')
@click.option(
    '--json',
    prompt='Path to JSON containing recipe',
    help="Path to JSON file that contains the recipe to add to database")
def add_recipe(json):
    """Adds new recipe (in JSON format) to database"""
    session = load_session()
    add_new_recipe(session, json)


@cli.command('init_db')
def init_db():
    """Reinitalizes database."""
    engine = create_engine(SQL_DB)
    Base.metadata.create_all(engine)


def load_session():
    engine = create_engine(SQL_DB)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


if __name__ == "__main__":
    cli()
