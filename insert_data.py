#!/usr/bin/ptyhon3
"""inserts data into storage"""
'''
from models.category import Category
from models.subcategory import Subcategory
from models.product import Product
from models.user import User
'''

categories = ["Beverages", "Staple/packaged_foods", "Snacks", "Cleaning/Hygiene", "Babys", "Alcoholic", "Hair_care"]
subcategories = {
        categories[0]: ["Soft_drinks", "Bottled_water", "Juice", "Energy_drings", "Malt_drinks"],
        categories[1]: ["Rice", "Instant_noodles", "Pasta", "Grains/Legiumes", "Cooking_ingredients", "Canned_foods", "Flour/Baking_supplies"],
        categories[2]: ["Biscuts", "Sweets"],
        categories[3]: ["Laundry/Detergents", "Toiletries", "Sanitizers"],
        categories[4]: ["Diapas", "Lotion/Oils", "Baby_formula&Food"],
        categories[5]: ["Wines", "Spirits"],
        categories[6]: ["Shampoos/Conditionsers", "Repaxers", "Oils/Creams", "Gels", "Extentions/Wigs"]
        }

brands = {
        "Beverages": [
            {"Soft_drinks": ["Coca-Cola", "Fanta", "Djino", "Vimto", "Orangina", "Sprite", "Planet", "Top", "Special"]},
        {"Bottled_water": ["Tangui", "Vital", "Opur", "Supermont"]},
        {"Juice": []},
        {"Energy_drings": ["Reactor"]},
        {"Malt_drinks": ["Guinness", "Ice", "Maltina"]}
            ],

        "Staple/packaged_foods": [
            {"Rice": ["Broli", "Bijou", "Ndop", "Uncle ben"]},
            {"Instant_noodles": ["Indomie", "Mimee"]},
            {"Pasta": ["Pasta gold", "Pazani"]},
            {"Boter": []},
            {"Mayonnaise": []},
            {"Milk": []},
            {"Grains/Legiumes": []},
            {"Cooking_ingredients": ["Maggi", "Palm-oil", "Groudnut-oil"]},
            {"Canned_foods": ["Sardines", "Mackerel", "Tomatos"]},
            {"Flour/Baking_supplies": []}
            ],

        "Snacks": [
            {"Biscuts": ["Parle-G", "Rio", "Ochoco"]},
            {"Sweets": []}
            ],

        "Cleaning/Hygiene": [
            {"Laundry/Detergents": ["Ozil", "Madar"]},
            {"Toiletries": ["Toilet Tissue"]},
            {"Sanitizers": []}
             ],

        "Babys": [
            {"Diapas": ["Dipas", "Pampas", "huggies"]},
            {"Lotion/Oils": []},
            { "Baby_formula&Food": ["Cerelac", "NAN"]}
             ],

        "Alcoholic": [
            {"Wines": ["Carlo", "Rossi"]},
            {"Spirits": ["schnapps", "Alomo Bitters"]}
             ],

        "Hair_care": [
            {"Shampoos/Conditionsers": []},
            {"Repaxers": ["MegaGrowth", "Ors olive oil"]},
            {"Oils/Creams": ["Motions", "MegaGrowth Relax"]},
            {"Gels": ["Dax", "Blue Magic", "Shea Butter"]},
            {"Extentions/Wigs": ["Darling hair", "X-pression", "Lush hair"]}
             ]

        }

for key in brands.keys():
    for sub in range(len(brands[key])):
        #print(products[key][sub])
        for items in brands[key][sub].keys():
            print(brands[key][sub][items])

'''
#create the categories:
for i in range(len(categories)):
    inst = Category()
    inst.name = catgories[i]
    inst.save()


#Create all subcategories
for key in subcategories.keys():
    category_list = models.storage.all('category')
    for item in category_list.keys():
        if category_list[item].name == key:
            category_id = category_list[item].id
            for j in range(len(subcategory[key])):
                inst = Subcategory()
                inst.category_id = category_id
                inst.name = subcategory[key][j]
                inst.save()

'''

