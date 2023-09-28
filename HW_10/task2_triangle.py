class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def existence_triangle(self):
        if self.side_a < self.side_b + self.side_c and self.side_b < self.side_a + self.side_c and \
                self.side_c < self.side_a + self.side_b:
            return (f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} - существует. '\
                    f'{self.type_triangle()}')
        else:
            return (f'Треугольника со сторонами {self.side_a}, {self.side_b}, {self.side_c} - не существует.')

    def type_triangle(self):
        if self.side_a == self.side_b == self.side_c:
            return ('Треугольник является равносторонним.')
        elif self.side_a == self.side_b or self.side_b == self.side_a or self.side_a == self.side_c:
            return ('Треугольник является равнобедренным.')
        elif self.side_c ** 2 == self.side_a ** 2 + self.side_b ** 2:
            return ('Треугольник является прямоугольным.')
        else:
            return ('Треугольник является разносторонним.')


triangle_1 = Triangle(4, 5, 6)
triangle_2 = Triangle(1, 2, 3)
triangle_3 = Triangle(5, 5, 5)
triangle_4 = Triangle(5, 5, 0)
triangle_5 = Triangle(5, 5, 2)
triangle_6 = Triangle(3, 4, 5)

for triangle in [triangle_1, triangle_2, triangle_3, triangle_4, triangle_5, triangle_6]:
    print(triangle.existence_triangle())
