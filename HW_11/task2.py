'''
Разработайте программу для хранения и управления текстовыми и числовыми записями.
Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:

Класс Archive должен иметь следующие атрибуты:

archive_text (list): Список архивированных текстовых записей.
archive_number (list): Список архивированных числовых записей.
text (str): Текущая текстовая запись, которую нужно добавить в архив.
number (int или float): Текущая числовая запись, которую нужно добавить в архив.
Класс Archive должен реализовать шаблон Singleton, чтобы гарантировать, что существует только один экземпляр архива.

Класс Archive должен иметь метод __init__(self, text: str, number: int | float), который принимает текстовую и числовую запись и сохраняет их как текущие записи для добавления в архив.

Класс Archive должен реализовать методы
__str__(self) и __repr__(self), чтобы можно было получить строковое представление текущих записей и архива.
'''

class Archive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.archive_number = []
            cls.archive_text = []
        else:
            cls._instance.archive_number.append(cls._instance.number)
            cls._instance.archive_text.append(cls._instance.text)
        return cls._instance

    def __init__(self, text, number):
        self.number = number
        self.text = text

    def __str__(self):

        return f'Text is {self.text} and number is {self.number}. Also {list(self.archive_text)} and {list(self.archive_number)}'

    def __repr__(self):
        return f'Archive({self.number},{self.text})'

# archive1 = Archive("First Text", 1)
# archive2 = Archive("Second Text", 2)
# archive3 = Archive("Third Text", 3)

archive4 = Archive("Запись 1", 42)
archive5 = Archive("Запись 2", 3.14)

# print(archive1.archive_text)  # Выведет: ['First Text', 'Third Text']
# print(archive1.archive_number)  # Выведет: [1, 3]
# print(archive2.archive_text)  # Выведет: ['First Text', 'Second Text']
# print(archive2.archive_number)
print(archive4)
print(archive5)