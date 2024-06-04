spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = []
    for item in spicy_foods:
        food_names.append(item['name'])
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciests_foods = []
    for item in spicy_foods:
        if item['heat_level'] > 5:
            spiciests_foods.append(item)
    return spiciests_foods

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {item['heat_level']* '🌶'}")
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_dict = []
    for item in spicy_foods:
        if item['cuisine'] == cuisine:
            return item
    

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item['heat_level'] > 5:
            print(f"{item['name']} ({item['cuisine']}) | Heat Level: {item['heat_level']* '🌶'}")


def get_average_heat_level(spicy_foods):
    average = 0
    for item in spicy_foods:
        average += item['heat_level']
    return average/3

        
def create_spicy_food(spicy_foods, spicy_food):
   spicy_foods.append(spicy_food)
   return spicy_foods
