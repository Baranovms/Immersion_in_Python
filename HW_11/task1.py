'''
Разработайте программное обеспечение для ведения журнала событий. Вам необходим класс, который будет представлять строки журнала и включать в себя информацию об авторе и времени создания каждой записи.

Создайте класс MyStr, который наследуется от встроенного класса str. Этот класс будет представлять строки с информацией о событиях.

Класс MyStr должен иметь следующие атрибуты:

value (str): Строковое значение с описанием события.
author (str): Имя автора, создавшего запись.
time (float): Время создания записи в формате '%Y-%m-%d %H:%M'.
Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author. Метод также автоматически фиксирует время создания записи.

Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr с информацией о событии, авторе и времени создания.

Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr для отладки.
'''

from datetime import datetime

class MyStr(str):
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.value = value
        instance.time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return instance
    
    def __str__(self) -> str:
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self) -> str:
        return f"MyStr('{self.value}', '{self.author}')"

event = MyStr("Завершилось тестирование", "John")
print(event)
print(repr(event))



#Вариант от GB
'''
import time
from datetime import datetime
class MyStr(str):
    """
    Класс для создания строки с информацией об авторе и времени создания.

    Атрибуты:
    value (str): строковое значение.
    author (str): имя автора.

    Dunder методы:
    __new__(cls, value, author): создает новый объект класса.
    __str__(): возвращает строковое представление объекта класса.
    __repr__(): возвращает строковое представление объекта класса для отладки.
    """
class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"
'''