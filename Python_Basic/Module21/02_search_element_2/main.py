import random


def find_key(my_dict, key, depth, depth_2):
	if key in my_dict:
		return my_dict[key]
	if depth > 1:
		for dep in my_dict.values():
			if isinstance(dep, dict):
				result = find_key(dep, key, depth - 1, depth_2)
				if result:
					break
		else:
			result = None
		return result


site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


key = input("Какой ключ ищем? ")
max_depth = input("Хотите ввести максимальную глубину? Y/N:").lower()

if max_depth == "y":
	depth = int(input("Введите максимальную глубину: "))
	value = find_key(site, key, depth, max_depth)
	print("Значение ключа: ", value)
elif max_depth == "n":
	depth = random.randint(2, 10)
	value = find_key(site, key, depth, max_depth)
	print("Значение ключа: ", value)




