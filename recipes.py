import requests
from pprint import pprint

"""Here is a program that will query the Edamam API with a particular ingredient.
It will return a list of recipes based on that particular query. 
You'll see a name, health labels, dietary cautions, a link and ingredients.
It will then ask the user if they'd like to save that into a list with the name of your searched item.
You'll get a final message to say goodbye."""

def recipe_searcher():
    ingredient = input("Hey there! I'm here to help you cook something new. Input one ingredient you'd like to use: ")
    app_id = "5d400412"
    app_key = "a985669be0ddaf3eea400aa1539561e5"
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    response = requests.get(url)
    recipes_general = response.json()
    recipes_individual = recipes_general['hits']
    print('\n' + 'Here\'s a list:' + '\n')
    name = []
    healthLabels = []
    cautions = []
    link = []
    ingredients = []
    for recipe in recipes_individual:
        print('Name: ' + str(recipe['recipe']['label']))
        name.append('Name: ' + ' '.join([recipe['recipe']['label']]))
        print('Health labels: ' + ', '.join(recipe['recipe']['healthLabels']))
        healthLabels.append('Health labels: ' + ', '.join(recipe['recipe']['healthLabels']))
        print('Dietary cautions: ' + ', '.join(recipe['recipe']['cautions']))
        cautions.append('Dietary cautions: ' + ', '.join(recipe['recipe']['cautions']))
        print('Link: ' + str(recipe['recipe']['shareAs']))
        link.append('Link: ' + str(recipe['recipe']['shareAs']))
        print('Ingredients: ' + ', '.join(recipe['recipe']['ingredientLines']))
        ingredients.append('Ingredients: ' + ', '.join(recipe['recipe']['ingredientLines']))
        print('\n')
    print('\n')
    text = input('Would you like me to save these to a file? y/n ')
    if text == "y":
        with open("%s.txt" % ingredient, 'x') as file:
            for i in range(len(name)):
                contents = str(name[i]) + '\n' + str(healthLabels[i]) + '\n' + str(cautions[i]) + '\n' + str(link[i]) + '\n' + str(ingredients[i]) +'\n' * 2
                file.write(contents)
    else:
        print('No problem, you can still access the recipes from the links above.')
    print('\n'+'All done. Bon appetit!')


recipe_searcher()

