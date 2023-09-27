'''
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
'''
import csv
from random import randint as r
from typing import Callable
import json
from pathlib import Path
from functools import wraps


def csv_file(func1: Callable) -> None:
    @wraps(func1)
    def wrapper(*args):
        with open("result.csv", 'r', newline='') as f:
            csv_file = csv.reader(f)
            for i, line in enumerate(csv_file):
                if i == 0:
                    continue
                else:
                    row = ''.join(line)
                    params = row.split()
                    params = [int(j) for j in params]
                    result = func1(params)
        return result
    return wrapper

def json_file(func: Callable):
    file = Path("result.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args):
        result = func(*args)
        d = {f"{args}":result,}
        data.append(d)

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return result
    return wrapper

@csv_file
@json_file
def solve_square_equation(list_of_num: list):
    a = list_of_num[0]
    b = list_of_num[1]
    c = list_of_num[2]
    x1 = x2 = None
    d = b * b - 4 * a * c
    
    if d > 0:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return round(x1, 2), round(x2, 2)
    elif d == 0:
        return round(-b/(2*a), 2)
    else:
        return "No answer"
    

def gen_csv(file_name: str) -> None:

    rows = r(100, 1001)
    count = 3

    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        for i in range(rows):
            lines = []
            for _ in range(count):
                a = r(1, 100)
                lines.append(a)
            if i == 0:
                csv_write.writerow(['A', 'B', 'C'])
            else:
                csv_write.writerow(lines)

if __name__ == '__main__':

    gen_csv("result.csv")
    solve_square_equation()
    