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
    names = [food["name"] for food in spicy_foods]
    return names
#print(get_names(spicy_foods))
def get_spiciest_foods(spicy_foods):
    spicy = [food for food in spicy_foods if food["heat_level"] > 5]
    return spicy

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        dish = food["name"]
        cuisine = food["cuisine"]
        chilli = '🌶' * food["heat_level"]
        print(f"{dish} ({cuisine}) | Heat Level: {chilli}")
#print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return spicy[0]
#print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

def print_spiciest_foods(spicy_foods):
    spicy = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spicy:
        dish = food["name"]
        cuisine = food["cuisine"]
        chilli = '🌶' * food["heat_level"]
        print(f"{dish} ({cuisine}) | Heat Level: {chilli}")

def get_average_heat_level(spicy_foods):
    levels = [food["heat_level"] for food in spicy_foods]
    return (sum(levels) / len(levels))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
