class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_matrix(self, matrix=None):
        if matrix is None:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    print(self.matrix[i][j], end=' ')
                print()
            print()
        else:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    print(matrix[i][j], end=' ')
                print()
            print()

    def transpose_matrix(self):
        t_matrix = [[0] * len(self.matrix) for i in range(len(self.matrix[0]))]
        for i in range(len(t_matrix)):
            for j in range(len(t_matrix[0])):
                t_matrix[i][j] = self.matrix[j][i]
        return t_matrix


def main():
    m_1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    m_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    matrixes = (m_1, m_2)
    for matrix in matrixes:
        matrix.print_matrix()
        matrix.print_matrix(matrix.transpose_matrix())


if __name__ == '__main__':
    main()