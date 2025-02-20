class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f'{key}:{value}')

    def get(self, key):
        if key in self.cache_dict:
            return self.cache_dict[key]
        else:
            return None

    @property
    def cache(self):
        if len(self.cache_dict) > 0:
            old_k = next(iter(self.cache_dict))
            print(f'{old_k}:{self.cache_dict[old_k]}')
        return self.cache_dict

    @cache.setter
    def cache(self, new_elem):
        if len(self.cache_dict) >= self.capacity:
            old_k = next(iter(self.cache_dict))
            del self.cache_dict[old_k]
        self.cache_dict[new_elem[0]] = new_elem[1]




# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4