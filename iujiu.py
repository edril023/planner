import os
import json

class RecipeDatabase:
    def __init__(self, folder='recipes'):
        self.recipe_folder = folder
        if not os.path.exists(self.recipe_folder):
            os.makedirs(self.recipe_folder)

    def register_recipe(self, name, recipe_type, ingredients, instructions):
        recipe_data = {
            'name': name,
            'type': recipe_type,
            'ingredients': ingredients,
            'instructions': instructions
        }
        with open(os.path.join(self.recipe_folder, f'{name}.json'), 'w') as f:
            json.dump(recipe_data, f, indent=4)
        print(f'Recipe Registered: {name} - {recipe_type}')
        print(f'Ingredients: {ingredients}')
        print(f'Instructions: {instructions}')
        return recipe_data

# Example usage
if __name__ == '__main__':
    db = RecipeDatabase()
    
    # Register a sample recipe
    recipe_name = 'Pancakes'
    recipe_type = 'Breakfast'
    recipe_ingredients = 'Flour, Eggs, Milk, Sugar, Baking Powder'
    recipe_instructions = '1. Mix ingredients\n2. Cook on a griddle\n3. Serve hot'

    db.register_recipe(recipe_name, recipe_type, recipe_ingredients, recipe_instructions)
