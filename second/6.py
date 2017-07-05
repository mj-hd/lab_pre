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
                result += "%d " % self[x, y]
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

        a = Matrix(self.width, self.height)
        l = Matrix(self.width, self.height)
        u = Matrix(self.width, self.height)

        for y in range(self.height):
            for x in range(self.width):
                a[x, y] = self[x, y]

        for i in range(self.height):
            lv = Matrix(1, self.height - i - 1)
            uv = Matrix(self.width - i - 1, 1)

            u[i, i] = 1

            # orange
            pivod = a[i, i]
            l[i, i] = pivod

            # red
            for j in range(i + 1, self.height):
                l[i, j] = a[i, j]
                lv[0, j - i - 1] = l[i, j]

            # blue
            for j in range(i + 1, self.width):
                u[j, i] = a[j, i] / pivod
                uv[j - i - 1, 0] = u[j, i]

            # green
            lu = lv * uv
            for x in range(i + 1, self.width):
                for y in range(i + 1, self.height):
                    a[x, y] = a[x, y] - lu[x - i - 1, y - i - 1]

        for n in range(self.width):
            s = 0
            for i in range(self.height):
                y = ((i == n ? 1 : 0) - s) / l[i, i]

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
