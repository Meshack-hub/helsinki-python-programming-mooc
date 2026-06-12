# Write your solution here
def search_by_name(filename: str, word: str):
    recipes = []
    with open(filename) as file:
        for row in file:
            row = row.strip()
            recipes.append(row)

    recipe_names = []
    i = 0
    start = True
    for item in recipes:
        if start:
            recipe_names.append(item)
        if item == "":
            recipe_names.append(recipes[i+1])
        if i == len(recipes) - 1:
            recipe_names.append(item)
        start = False
        i += 1

    fnd_recipes = []
    for name in recipe_names:
        if word.lower() in name.lower():
            fnd_recipes.append(name)

    return fnd_recipes

def search_by_time(filename: str, prep_time: int):
    recipes = []
    with open(filename) as file:
        for row in file:
            row = row.strip()
            recipes.append(row)
    
    recipes_time = {}
    start = True
    i = 0
    for item in recipes:
        if start:
            recipes_time[item] = int(recipes[i+1])
        if item == "":
            recipes_time[recipes[i+1]] = int(recipes[i+2])
        start = False
        i += 1

    fnd_recipe = []
    for name, time in recipes_time.items():
        if time <= prep_time:
            fnd_recipe.append(f"{name}, preparation time {time} min")

    return fnd_recipe

def search_by_ingredient(filename: str, ingredient: str):
    recipe_ingredients = {}
    recipes = []
    with open(filename) as file:
        lines = file.readlines()
        for row in lines:
            row = row.strip()
            if row != "":
                recipes.append(row)
            else:
                recipe_ingredients[recipes[0]] = recipes[1:]
                recipes = []
            
        if recipes:
            recipe_ingredients[recipes[0]] = recipes[1:]

    fnd_recipe = []
    for recipe, items in recipe_ingredients.items():
        time = items[0]
        ingredients = items[1:]

        for ing in ingredients:
            if ingredient.lower() in ing.lower():
                fnd_recipe.append(f"{recipe}, preparation time {time} min")
                break #avoid duplicates
    return fnd_recipe


if __name__ == "__main__":      
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
    print()

    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)
    print()

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
        











