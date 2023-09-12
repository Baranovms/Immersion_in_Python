'''
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''

import os

string = "C:/Users/user/Downloads/Education/Immersion_in_Python/HW_5/task2.py"

def fun(f_path):
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string} \nКортеж из пути: {fun(string)}')