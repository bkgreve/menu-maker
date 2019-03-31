from sqlalchemy import Integer, ForeignKey, String, Column, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    recipe_type = Column(String(20))
    meat = Column(String(20))
    diet = Column(String(20))

    ingredients = relationship("RecipeIngredient", back_populates="recipe")
    instructions = relationship("Instruction", back_populates="recipe")


class Ingredient(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredient'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'))
    quantity = Column(FLOAT)
    units = Column(String(10))

    recipe = relationship("Recipe", back_populates="ingredients")


class Instruction(Base):
    __tablename__ = 'instruction'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe_instructions = Column(String(1000))

    recipe = relationship("Recipe", back_populates="instructions")
