'''
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

from os import listdir, mkdir, chdir
from pathlib import Path


def get_extensions (data: list[str]):
    data = set(map(lambda x: x.split('.')[-1], data))
    return list(data)


def sort_files(working_dir = 'HW_7/file_for_task6'):
    data = get_extensions(listdir(Path(working_dir)))
    chdir(Path(working_dir))
    for ext in data:
        try:
            mkdir(ext)
        except FileExistsError:
            pass
    for file in filter(lambda x: x.find('.') != -1, listdir()):
        prev = Path(file)
        prev.replace(Path.cwd() / file.split('.')[-1] / prev)


sort_files()