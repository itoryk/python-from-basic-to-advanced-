goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product_name, product_code in goods.items():
    product_quantity = 0
    product_value = 0
    for position in store[product_code]:
        product_quantity += position['quantity']
        product_value += position['quantity'] * position['price']

    print(product_name, '-', product_quantity, 'штук, стоимость', product_value, 'рубля')