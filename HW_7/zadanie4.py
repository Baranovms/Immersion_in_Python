'''
#### zadanie4
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
-расширение
-минимальная длина случайно сгенерированного имени, по умолчанию 6
-максимальная длина случайно сгенерированного имени, по умолчанию 30
-минимальное число случайных байт, записанных в файл, по умолчанию 256
-максимальное число случайных байт, записанных в файл, по умолчанию 4096
-количество файлов, по умолчанию 42
-Имя файла и его размер должны быть в рамках переданного диапазона.
'''

from string import ascii_letters
from random import randint, choices, randbytes

_MIN_LEN_NAME = 6
_MAX_LEN_NAME = 30
_MIN_SIZE = 256
_MAX_SIZE = 4096

def create_file(extension, count_files = 42):
    for _ in range(count_files):
        lenght_name = randint(_MIN_LEN_NAME, _MAX_LEN_NAME)
        file_name = ''.join(choices(ascii_letters, k=lenght_name)) + extension
        size = randint(_MIN_SIZE, _MAX_SIZE)
        with open(file_name, 'wb') as f:
            f.write(randbytes(size))

if __name__ == '__main__':
    create_file('.txt')