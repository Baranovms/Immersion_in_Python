
import os
import logging
from collections import namedtuple

# Установка уровня логирования
logging.basicConfig(filename='log.txt',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Определение namedtuple
File = namedtuple('File', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_file_information(directory_path):
    for root, directories, files in os.walk(directory_path):
        for file in files:
            name, extension = os.path.splitext(file)
            parent_directory = os.path.basename(root)
            is_directory = False
            logging.info(f"File: {name} / Extension: {extension} / Parent Directory: {parent_directory}")
            yield File(name, extension, is_directory, parent_directory)
        for directory in directories:
            name = directory
            extension = None
            parent_directory = os.path.basename(root)
            is_directory = True
            logging.info(f"Directory: {name} / Parent Directory: {parent_directory}")
            yield File(name, extension, is_directory, parent_directory)

if __name__ == "__main__":
    directory_path = input("Введите путь до директории: ")
    for file_info in get_file_information(directory_path):
        print(file_info)