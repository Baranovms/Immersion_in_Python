'''
Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:

Инициализация матрицы. Конструктор класса должен принимать количество строк rows и количество столбцов cols и создавать матрицу с нулевыми значениями.

Операция сложения матриц. Реализуйте метод __add__, который позволяет складывать две матрицы одинаковых размеров.

Операция умножения матриц. Реализуйте метод __mul__, который позволяет умножать две матрицы с согласованными размерами (количество столбцов первой матрицы 
должно быть равно количеству строк второй матрицы).

Сравнение матриц на равенство. Реализуйте метод __eq__, который позволяет сравнивать две матрицы на равенство.

Представление матрицы в виде строки. Реализуйте метод __str__, который возвращает строковое представление матрицы, где элементы строки разделены пробелами, 
а строки сами разделены символами новой строки.

Представление матрицы в виде строки для создания нового объекта. Реализуйте метод __repr__, который возвращает строку, которую можно использовать для создания 
нового объекта класса Matrix.
'''


class Matrix:  
    def __init__(self, rows, columns):  
        self.rows = rows  
        self.columns = columns  
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]  
   
    def __add__(self, other):  
        if self.rows != other.rows or self.columns != other.columns:  
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")  
        result = Matrix(self.rows, self.columns)  
        for i in range(self.rows):  
            for j in range(self.columns):  
                result.data[i][j] = self.data[i][j] + other.data[i][j]  
        return result  
    
    def __mul__(self, other):  
        if self.columns != other.rows:  
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")  
        result = Matrix(self.rows, other.columns)  
        for i in range(self.rows):  
            for j in range(other.columns):  
                for k in range(self.columns):  
                    result.data[i][j] += self.data[i][k] * other.data[k][j]  
        return result  

    def __str__(self):  
        # output = ""  
        # for row in self.data:  
        #     output = " ".join(str(element) for element in row) + "\n"  
        # return output 
        return '\n'.join([' '.join(map(str, row)) for row in self.data]) 
    
    def __repr__(self) -> str:
        return f'Matrix({self.data})'


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)


# Ожидаемый ответ:

# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# False
# 8 10 12
# 14 16 18
# 25 28
# 57 64
# 89 100