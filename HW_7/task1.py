'''
Напишите функцию группового переименования файлов. Она должна:
-принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
-принимать параметр количество цифр в порядковом номере.
-принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
-принимать параметр расширение конечного файла.
-принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
-Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''

import os

def batch_rename(new_name, digits, in_ext, out_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(in_ext):
            old_name = os.path.splitext(filename)[0] 
            if range_name:
                old_name_substring = old_name[range_name[0]:range_name[1]] 
            new_name = f"{old_name_substring}{new_name}{str(counter).zfill(digits)}{out_ext}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
            counter += 1



if __name__ == '__main__':
    batch_rename('new_file', 3, '.txt', '.md', [1, 3], 'HW_7/file_for_task6/txt')