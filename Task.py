#Task 1
def geometric_progression(a1, r):

    n = 0
    while True:
        yield a1 * (r ** n)
        n += 1

if __name__ == "__main__":
    a1 = 2
    r = 3

    gp_generator = geometric_progression(a1, r)

    for _ in range(10):
        print(next(gp_generator))

#Task 2
def my_range(start=0, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("Крок не може бути нульовим.")

    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

if __name__ == "__main__":
    print("my_range(5):")
    for num in my_range(5):
        print(num)

    print("\nmy_range(2, 5):")
    for num in my_range(2, 5):
        print(num)

    print("\nmy_range(1, 10, 2):")
    for num in my_range(1, 10, 2):
        print(num)

    print("\nmy_range(10, 0, -2):")
    for num in my_range(10, 0, -2):
        print(num)

#Task 3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    for num in range(2, limit):
        if is_prime(num):
            yield num

if __name__ == "__main__":
    upper_limit = 30
    print(f"Прості числа до {upper_limit}:")
    for prime in generate_primes(upper_limit):
        print(prime)

#Task 4
from datetime import datetime, timedelta

def date_generator(start_date, end_date):
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

if __name__ == "__main__":
    start = '2023-01-01'
    end = '2023-01-07'

    print(f"Послідовність дат з {start} до {end}:")
    for date in date_generator(start, end):
        print(date.strftime('%Y-%m-%d'))