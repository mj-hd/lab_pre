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

    # get transposed self
    def transpose(self):
        result = Matrix(self.height, self.width)

        for y in range(self.height):
            for x in range(self.width):
                result[y, x] = self[x, y]

        return result


a = Matrix(3, 3)
b = Matrix(3, 3)

print "input matrix A(3x3, each number must be separated by RETURN):"
for y in range(a.height):
    for x in range(a.width):
        a[x, y] = input()

print "input matrix B(3x3, each number must be separated by RETURN):"
for y in range(b.height):
    for x in range(b.width):
        b[x, y] = input()

t = a.transpose()

print "A:"
print a

print "B:"
print b

print "T:"
print t

print "TxB:"
print t.cross(b)
