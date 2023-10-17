from typing import Union
class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

class InvalidTextError(Exception):
    def __init__(self,text) -> None:
        self.text = text

    def __str__(self) -> str:
        super().__str__(self)    
        if type(self.text) != 'str' or self.text == '':
            return f'Не является текстом или пустой или является пустой строкой'

class InvalidNumberError(Exception):
    def __init__(self,number) -> None:
        self.number = number
        
    def __str__(self) -> str:
        super().__str__(self)
        if (self.number < 0 or type(self.number) != 'int' or type(self.number) != 'float'):
            return f'Не является положительным целым или числом с плавающей запятой'


if __name__ == '__main__':
    try:
        invalid_archive_instance = Archive("Sample text", -5)
        print(invalid_archive_instance)
    except Exception as e:
        print(e)
