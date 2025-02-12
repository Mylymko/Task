# Task1
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції '{func.__name__}' з аргументами: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функція '{func.__name__}' завершилася з результатом: {result}")
        return result
    return wrapper
@my_decorator
def add(a, b):
    return a + b
@my_decorator
def multiply(a, b):
    return a * b
add(5, 3)
multiply(4, 2)

# Task2
import json
import os
from functools import wraps
def cache_to_file(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            key = str(args)
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    cached_results = json.load(f)
            else:
                cached_results = {}
            if key in cached_results:
                print(f"Використання кешованого результату для {key}")
                return cached_results[key]
            result = func(*args)
            cached_results[key] = result
            with open(filename, 'w') as f:
                json.dump(cached_results, f)
            return result
        return wrapper
    return decorator
@cache_to_file('results.json')
def add(a, b):
    return a + b
if __name__ == "__main__":
    print(add(5, 3))
    print(add(5, 3))
    print(add(4, 2))

# Task3
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль.")
        except TypeError as e:
            print(f"Помилка: Неправильний тип аргументів. {e}")
        except Exception as e:
            print(f"Виникла помилка: {e}")
    return wrapper
@handle_exceptions
def divide(a, b):
    return a / b
print(divide(5, 0))
print(divide(5, 2))
print(divide(5, 'a'))

#Task4
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання '{func.__name__}': {execution_time:.6f} секунд")
        return result
    return wrapper
@measure_time
def some_function():
    time.sleep(2)
some_function()

#Task5
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s • %(levelname)s • %(message)s')
logger = logging.getLogger(__name__)
def log_arguments_results(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Виклик функції '{func.__name__}' з аргументами: {args} та {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Результат функції '{func.__name__}': {result}")
        return result
    return wrapper
@log_arguments_results
def add_numbers(a, b):
    return a + b
add_numbers(3, 4)

#Task6
def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                print(f"Функція '{func.__name__}' досягла максимальної кількості викликів: {max_calls}.")
                return None
        return wrapper
    return decorator
@limit_calls(3)
def some_function():
    print("Виклик функції")
some_function()
some_function()
some_function()
some_function()

#Task7
def cache_results(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Використання кешу для {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(5))
print(fibonacci(5))