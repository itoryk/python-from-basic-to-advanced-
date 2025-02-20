import time


def memorize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper


@memorize
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


start_time = time.perf_counter()
print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(5))
end_time = time.perf_counter()
print(f'Время выполнения: {end_time - start_time:.8f} секунд')
