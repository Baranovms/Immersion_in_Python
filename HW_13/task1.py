'''
расчет площади, периметра прямоугольника,
селадывание и вычитание двух прямоугольников

'''
class NegativeValueError:
    def __init__(self, min_value: int = 1) -> None:
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError('Invalid type of input')
        if value < self.min_value:
            raise ValueError('Invalid value of input')


class Rectangle:
    width = NegativeValueError()
    height = NegativeValueError()

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height
    
    def __add__(self,other):
        return Rectangle(self.width + other.width, self.height + other.height)
    
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __str__(self) -> str:
        return f"Прямоугольник со сторонами {self.width} и {self.height}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.width}, {self.height}"

r = Rectangle(-2)

# class NegativeValueError(Exception):
#     def __init__(self, min_value: int = 1):
#         self.min_value = min_value

#     def __str__(self):
#         if self.width <= 0 and self.height <= 0:
#             return f"Стороны должны быть положительными, а не {self.width}; {self.height}"
#         else:
#             if self.width == self.height and self.width < 0:
#                 return f"Ширина должна быть положительной, а не {self.width} "
#             if self.width <= 0 or self.width == self.height:
#                 return f"Ширина должна быть положительной, а не {self.width} "
#             else:
#                 return f"Высота должна быть положительной, а не {self.height}"


# class Rectangle:

#     def __init__(self, width: float, height: float):
#         self._side_a = width
#         self._side_b = height if height else width

#     def get_perimeter(self):
#         return 2 * (self._side_a + self._side_b)

#     def get_area(self):
#         return self._side_a * self._side_b

#     def __str__(self):
#         return f"В результате - прямоугольник со сторонами: {self._side_a}   {self._side_b}, периметром: {self.get_perimeter()}, площадью: {self.get_area()}"
    

