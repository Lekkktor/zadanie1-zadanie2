from pprint import pprint
cook_book = {}
with open('book.txt', encoding= 'utf-8') as file:
    recept = {}
    for line in file:
        name = line.strip()
        ingridients = int(file.readline())
        employse = []
        for i in range(ingridients):
            ingridient_name, quantity, measure = file.readline().strip().split(' | ')
            employse.append({'ingridient name': ingridient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        recept[name] = employse
    pprint(recept,  width=100, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        for item in (recept[dish]):
            items_list = dict([(item['ingridient name'], {'measure': item['measure'], 'quantity': int(item['quantity']) * person_count})])
            if shopping_list.get(item['ingridient name']):
                extra_item = (int(shopping_list[item['ingridient name']]['quantity']) + int(items_list[item['ingridient name']]['quantity']))
                shopping_list[item['ingridient name']]['quantity'] = extra_item

            else:
                shopping_list.update(items_list)

        print(f"Для приготовления блюд на {person_count} человек  нам необходимо купить:")
        pprint(shopping_list)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)