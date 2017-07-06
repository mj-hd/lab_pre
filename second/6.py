#!/usr/bin/python

# represent a matrix
class Matrix:
    # construct a width x height matrix
    def __init__(self, width, height):
        self.mat = [[0 for x in range(width)] for y in range(height)]
        self.width  = width
        self.height = height

    # matrix[x, y]
    def __getitem__(self, p):
        x, y = p
        if x >= self.width or y >= self.height or x < 0 or y < 0:
            raise IndexError()

        return self.mat[y][x]

    def __setitem__(self, p, value):
        x, y = p
        if x >= self.width or y >= self.height or x < 0 or y < 0:
            raise IndexError()

        self.mat[y][x] = value

    # convert the matrix to string
    def __str__(self):
        result = ""

        for y in range(self.height):
            result += " [ "
            for x in range(self.width):
                result += str(self[x, y]) + " "
            result += "]\n"

        return result

    def __repr__(self):
        return self.__str__()

    # get self x target
    def cross(self, target):
        if self.width != target.height:
            raise ArithmetricError()

        result = Matrix(target.width, self.height)

        for y in range(self.height):
            for x in range(self.width):
                result[x, y] = 0
                for i in range(self.width):
                    result[x, y] += self[i, y] * target[x, i]

        return result

    # get mult self and other
    def __mul__(self, other):
        if not(isinstance(other, self.__class__)):
            result = Matrix(self.width, self.height)
            for y in range(self.height):
                for x in range(self.width):
                    result[x, y] = other * self[x, y]

        result = Matrix(self.height, other.width)

        for y in range(self.height):
            for x in range(other.width):
                result[x, y] = 0
                for i in range(self.width):
                    result[x, y] += self[i, y] * other[x, i]

        return result

    # get transposed self
    def transpose(self):
        result = Matrix(self.height, self.width)

        for y in range(self.height):
            for x in range(self.width):
                result[y, x] = self[x, y]

        return result

    # get inverted self
    def invert(self):
        if self.width != self.height:
            raise NotImplemented()

        # result matrix
        result = Matrix(self.width, self.height)

        # lu decomposition matrices
        a = Matrix(self.width, self.height)
        l = Matrix(self.width, self.height)
        u = Matrix(self.width, self.height)

        # copy items from self to a
        for y in range(self.height):
            for x in range(self.width):
                a[x, y] = float(self[x, y])

        # lu decomposition
        # http://qiita.com/edo_m18/items/1d67532bed4a083cddb3
        for i in range(self.height):
            lv = Matrix(1, self.height - i - 1)
            uv = Matrix(self.width - i - 1, 1)

            u[i, i] = 1.

            # l0_0
            pivod = a[i, i]
            l[i, i] = pivod

            # l1
            for j in range(i + 1, self.height):
                l[i, j] = a[i, j]
                lv[0, j - i - 1] = l[i, j]

            # ->u1^T
            for j in range(i + 1, self.width):
                u[j, i] = a[j, i] / pivod
                uv[j - i - 1, 0] = u[j, i]

            # lu
            lu = lv * uv

            # a
            for x in range(i + 1, self.width):
                for y in range(i + 1, self.height):
                    a[x, y] = a[x, y] - lu[x - i - 1, y - i - 1]

        # calculate each column of result
        for n in range(self.width):
            x = [0] * self.height # solution
            y = [0] * self.height

            # y
            for i in range(self.height):
                s = 0.
                for j in range(i + 1):
                    s += l[j, i] * y[j]

                y[i] = ((1. if i == n else 0.) - s) / l[i, i]
            
            # x
            for i in range(self.width - 1, -1, -1):
                s = 0.
                for j in range(i + 1, self.width):
                    s += u[j, i] * x[j]

                x[i] = y[i] - s

            # copy result
            for i in range(self.height):
                result[n, i] = x[i]

        return result

a = Matrix(4, 4)

print "input matrix A(4x4, each number must be separated by RETURN):"
for y in range(a.height):
    for x in range(a.width):
        a[x, y] = input()

a_1 = a.invert()

print "A:"
print a

print "A-1:"
print a_1
