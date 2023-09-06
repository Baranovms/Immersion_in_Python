'''
Напишите функцию для транспонирования матрицы
'''

# Функция вывода матрицы
def print_matrix(input_matrix):
    for col in input_matrix:
        for row in col:
            print(row, "\t", end="")
        print()

# функция транспонирования (поворота на 90 градусов) матрицы
def matrix_transposition(input_matrix):
    end_matrix = []
    list_in_matrix = []
    count_start = 0
    count_stop = 1
    while count_start <= len(matrix):
        for col in input_matrix:
            for row in col[count_start:count_stop:]:
                list_in_matrix.append(row)
        end_matrix.append(list_in_matrix)
        list_in_matrix = []
        count_start += 1
        count_stop += 1
    return end_matrix


matrix = [[1, 2, 3], [4, 5, 6]]
print_matrix(matrix)
print()
print_matrix(matrix_transposition(matrix))