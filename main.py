# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import functools
import json
import math
from random import randint


def find_square(a=0, b=0, c=0):
    discr = b * b - 4 * a * c
    if discr >= 0:
        x1 = round((-b + math.sqrt(discr)) / (2 * a), 3)
        x2 = round((-b - math.sqrt(discr)) / (2 * a), 3)
        return (x1, x2)
    else:
        return ('Корней нет')

# print(find_square(3.2, -7.8, 1))

def generation_num(row):
    with open('example.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(row):
            writer.writerow([randint(0, 100) for _ in range(3)])


# generation_num(10)

def square_from_csv(func):
    @functools.wraps(func)
    def wrapper():
        results = []
        with open('example.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results

    return wrapper


a = square_from_csv(find_square)
# print(a())

def save_results_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('results.json', 'w', encoding='utf-8') as file:
            json.dump({'result': result}, file, indent=3, ensure_ascii=False)
        return result

    return wrapper


b = save_results_json(a)
b()
