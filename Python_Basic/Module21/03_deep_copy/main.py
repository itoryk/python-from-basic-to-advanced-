import copy
from pprint import pprint



site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def key_search(dictionary, key, value):
    if key in dictionary:
        dictionary[key] = value
        return site
    for level in dictionary.values():
        if isinstance(level, dict):
            result = key_search(level, key, value)
            if result:
                return site


def pretty_dict(my_dict, depth):
    for elem in my_dict:
        print('\t' * depth, elem)
        if isinstance(my_dict[elem], dict):
            pretty_dict(my_dict[elem], depth + 1)
        else:
            print('\t' * (depth + 1), ''.join(my_dict[elem]))


number_of_sites = int(input('Сколько сайтов: '))

d_copy = dict()
products = dict()
depth = 0
for _ in range(number_of_sites):
    is_name = input('Введите название продукта для нового сайта: ')
    key = {'title': f'Куплю/продам {is_name} недорого', 'h2': f'У нас самая низкая цена на {is_name}'}
    for x in key:
        key_search(site, x, key[x])
    name = f'Cайт для {is_name}'
    d_copy = copy.deepcopy(site)
    products[name] = d_copy
    pretty_dict(products, depth)