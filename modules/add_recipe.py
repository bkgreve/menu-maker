import json
import sys

from database.meal_maker_db import Recipe, Ingredient, RecipeIngredient, Instruction


def add_new_recipe(session, json_file):
    """Adds new recipe from JSON to database"""

    with open(json_file, 'r') as f:
        new_recipe = json.load(f)

    recipe_name = new_recipe['name']
    recipe_exists = session.query(
        Recipe.id).filter_by(name=recipe_name).scalar() is not None

    if not recipe_exists:
        recipe = Recipe(
            name=new_recipe['name'],
            recipe_type=new_recipe['recipe_type'],
            meat=new_recipe['meat'],
            diet=new_recipe['diet'])
        session.add(recipe)
        session.commit()
    else:
        print(f"{new_recipe['name']} already exists!")
        sys.exit()

    for ingredient in new_recipe['ingredients']:
        ingredient_exists = session.query(Ingredient.id).filter_by(
            name=ingredient["name"]).scalar() is not None
        if not ingredient_exists:
            new_ingredient = Ingredient(name=ingredient['name'])
            session.add(new_ingredient)
            session.commit()
            recipe_ingredient = RecipeIngredient(
                recipe_id=recipe.id,
                ingredient_id=new_ingredient.id,
                quantity=ingredient['quantity'],
                units=ingredient['units'])
            session.add(recipe_ingredient)
            session.commit()
        else:
            known_ingredient = session.query(Ingredient).filter_by(
                name=ingredient["name"]).first()
            recipe_ingredient = RecipeIngredient(
                recipe_id=recipe.id,
                ingredient_id=known_ingredient.id,
                quantity=ingredient['quantity'],
                units=ingredient['units'])
            session.add(recipe_ingredient)
            session.commit()

    instructions = Instruction(
        recipe_id=recipe.id, recipe_instructions=new_recipe['steps'])
    session.add(instructions)
    session.commit()

    print(f"{new_recipe['name']} has been added to the database.\n")
