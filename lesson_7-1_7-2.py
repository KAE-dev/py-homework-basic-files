from pprint import pprint


def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            name_of_the_dish = line.strip()
            number_of_ingredients = int(file.readline())
            ingredients_list = []
            for ingredient in range(number_of_ingredients):
                ingredient_name, quantity, unit_of_measurement = file.readline().split('|')
                ingredients_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': unit_of_measurement}
                )
            result[name_of_the_dish] = ingredients_list
            file.readline()
    return result


cook_book = prepare_dict("resources/cook/recipes.txt")


def get_shop_list_by_dishes(dishes, person_count):
    new_shop_dict = {}
    for dish in dishes:
        ingredients = cook_book.get(dish)
        for composition in ingredients:
            ingredient_name, quantity, measure = composition.values()
            quantity_with_person = int(quantity) * person_count
            if ingredient_name in new_shop_dict:
                quantity_with_person += new_shop_dict.get(ingredient_name).get('quantity')
            new_shop_dict[ingredient_name] = {
                'measure': measure, 'quantity': quantity_with_person
            }
    return new_shop_dict


shop_list_by_dishes = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
pprint(shop_list_by_dishes)
