#!/usr/bin/python

import math
from math import inf

def recipe_batches(recipe, ingredients):
  # look into this:
  # recipe_set= set(recipe.keys()))
  # ingredients_set = set(ingredients.keys())
  min_num_batches = inf
  ingredient_keys = ingredients.keys()
  for key in recipe.keys():
    if key in ingredient_keys:
      curr_batches = ingredients[key]//recipe[key]
      print(key,curr_batches)
      if min_num_batches > curr_batches:
        min_num_batches = curr_batches
        print(min_num_batches)
      pass
    else:
      return 0
  return min_num_batches
  



  # check if we have all ingredients
  # if we do:
    # pull just those ingredients out? (we don't care about the rest of the ingredients )
    # divide the ingredients values by the recepie values
    # return the minimumn value of the divisions.
  # if we don't
    # return 0 cause we can't make it

  # The plan changed cause you actually only need to keep track of the minimum number
  # of batches as you go along, instead of keeping track of everything. this way you

  # it might be slightly more effient to check if all the ingredients exist in the first place 
  # using some sort of set operation. But this depends on the efficiency of sets in general.


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 51, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))