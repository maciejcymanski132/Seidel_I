import random as rnd
import numpy as np


class Seidel:

    def only_one_right(self, vector):
        constr = len(vector)
        git = True
        for i in range(0, constr):
            if vector[i][0] != 0:
                git = False
        return git

    def only_one_left(self, vector):
        constr = len(vector)
        git = True
        for i in range(0, constr):
            if vector[i][1] != 0:
                git = False
        return git

    def gauss(self, vector_a, vector_b):
        constr = len(vector_a)
        matrix = [[0, 0, 0], [0, 0, 0]]
        xVector = [0] * constr
        for i in range(0, constr):
            for j in range(0, 2):
                matrix[i][j] = vector_a[i][j]

            matrix[i][constr] = vector_b[0][i]

        var = 0
        h = 0

        for j in range(0, constr):
            for i in range(0, constr):
                if (i != j):
                    var = matrix[i][j] / matrix[j][j]

                    for k in range(0, constr):
                        h = var * matrix[j][k]
                        matrix[i][k] = matrix[i][k] - h
        for i in range(0, constr):
            xVector[i] = matrix[i][constr] / matrix[i][i]
        print("gauss tutaj:", xVector)
        return xVector

    def seidel(self, vector_a, vector_b, vector_c):
        Xi = [0] * 2
        constr = len(vector_a)
        one_variable_left = self.only_one_left(vector_a)
        one_variable_right = self.only_one_right(vector_b)

        if one_variable_left:
            max = 0
            for i in range(0, constr):
                if max < vector_c[0] * vector_a[i][0]:
                    max = vector_c[0] * vector_a[i][0]
                    Xi[0] = vector_b[i] / (vector_a[i][0] + vector_a[i][1])
            Xi[1] = 0
            return Xi

        if one_variable_right:
            max = 0
            for i in range(0, constr):
                if max < vector_c[1] * (vector_b[i] / (vector_a[i][0] + vector_a[i][1])):
                    max = vector_c[1] * (vector_b[i] / (vector_a[i][0] + vector_a[i][1]));
                    Xi[1] = vector_b[i] / (vector_a[i][0] + vector_a[i][1]);
            Xi[0] = 0
            return Xi
        if len(vector_a) == len(vector_a[0]):
            print('Gauss')
            Xi = self.gauss(vector_a, vector_b)
            return Xi

        completelyRandomInteger = rnd.randint(0, constr - 1)
        print(completelyRandomInteger)
        erasedRow = [0] * 3
        erasedRow[0] = vector_a[completelyRandomInteger][0]
        erasedRow[1] = vector_a[completelyRandomInteger][1]
        erasedRow[2] = vector_b[0][completelyRandomInteger]
        vector_a.pop(completelyRandomInteger)
        vector_b[0].pop(completelyRandomInteger)

        Xi = self.seidel(vector_a, vector_b, vector_c)

        print(f"{Xi[0]} {Xi[1]}\n")

        if (erasedRow[0] * Xi[0] + (erasedRow[1] * Xi[1])) <= erasedRow[2]:
            return Xi
        else:
            constr_after_deletion = len(vector_a)
            change = [0] * 2
            change[0] = -1.0 * erasedRow[1] / erasedRow[0]
            change[1] = erasedRow[2] / erasedRow[0]
            for i in range(0, constr_after_deletion):
                vector_a[i][1] += change[0] * vector_a[i][0]
                vector_b[0][i] += -1.0 * change[1] * vector_a[i][0]
                vector_a[i][0] = 0
            return self.seidel(vector_a, vector_b, vector_c)


if __name__ == '__main__':
    s = Seidel()
    matrixA = [[-1, 1], [-1, 1], [-1, 1]]
    matrixB = [[1, 2, 3]]
    function = [-1, 1]

    constraints = len(matrixA)

    for i in range(0, constraints):
        for j in range(0, 2):
            print(matrixA[i][j])
        print("<=")

    xopt = s.seidel(matrixA, matrixB, function)

    if xopt[0] < 0:
        xopt[0] = 0
    if xopt[1] < 0:
        xopt[1] = 0

    print(f"x1 = {xopt[0]}, x2 = {xopt[1]}")
