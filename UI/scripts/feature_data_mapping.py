product_categories = {
     29: 'Soft Drink/Water',
     37: 'Mult Food Dinner/Grav/Sauce/Special',
     34: 'Choc/Cocoa Prod',
     46: 'Food Additives (Human Use)',
     53: 'Cosmetics',
     12: 'Cheese/Cheese Prod',
     15: 'Egg/Egg Prod',
     30: 'Beverage Bases/Conc/Nectar',
     13: 'Ice Cream Prod',
     33: 'Candy W/O Choc/Special/Chew Gum',
     14: 'Filled Milk/Imit Milk Prod',
     9: 'Milk/Butter/Dried Milk Prod',
     54: 'Vit/Min/Prot/Unconv Diet(Human/Animal)',
     20: 'Fruit/Fruit Prod',
     26: 'Vegetable Oils',
     32: 'Alcoholic Beverage',
     31: 'Coffee/Tea',
     7: 'Snack Food Item',
     5: 'Cereal Prep/Breakfast Food',
     38: 'Soup',
     45: 'Food Additives (Human Use)',
     3: 'Bakery Prod/Dough/Mix/Icing',
     21: 'Fruit/Fruit Prod',
     27: 'Dressing/Condiment',
     4: 'Macaroni/Noodle Prod',
     25: 'Vegetables/Vegetable Products',
     41: 'Dietary Conv Food/Meal Replacements',
     23: 'Nuts/Edible Seed',
     18: 'Vegetable Protein Prod',
     52: 'Miscellaneous Food Related Items',
     17: 'Meat, Meat Products and Poultry',
     35: 'Gelatin/Rennet/Pudding Mix/Pie Filling',
     36: 'Food Sweeteners (Nutritive)',
     39: 'Prep Salad Prod',
     16: 'Fishery/Seafood Prod',
     51: 'Food Service/Conveyance',
     2: 'Whole Grain/Milled Grain Prod/Starch',
     40: 'Baby Food Prod',
     22: 'Fruit/Fruit Prod',
     50: 'Color Additiv Food/Drug/Cosmetic',
     24: 'Vegetables/Vegetable Products',
     28: 'Spices, Flavors And Salts'
}


def get_symptom_list():
    return [
        'diarrhea',
        'mood_swing',
        'renal_function',
        'upper_respiratory_tract_infection',
        'prothrombin_time',
        'bleeding',
        'nasal_congestion',
        'drug_overdose',
        'angina',
        'dysbiosis',
        'overactive_bladder',
        'suicide_terminology',
        'epileptic_seizure',
        'nephrotoxicity',
    ]


def get_product_category_mappings():
    product_category_mappings = {}

    for product_key in product_categories.keys():
        product_category_mappings[product_key] = {
            'id': product_key,
            'name': product_categories[product_key]
        }

    return product_category_mappings


def to_number(number_as_string):
    age = 0
    if number_as_string is not None or number_as_string != '':
        age = int(number_as_string)

    return age