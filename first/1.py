#!/usr/bin/python

from cmath import sqrt

# represent a formula
# e.g. F(1, 2, 3) => x^2 + 2x + 3
class F:
    def __init__(self, *coefs):
        self.coefs = coefs

    # calculate a value for x
    def __getitem__(self, x):
        result = 0

        i = len(self.coefs)
        for coef in self.coefs:
            i -= 1
            result += coef * x**i

        return result

    # convert the formula to string
    def __str__(self):
        result = ""

        i = len(self.coefs)
        for coef in self.coefs:
            i -= 1
            result += " %d x^%d +" % (coef, i)

        result = result[:-1]

        return result

    def __repr__(self):
        return self.__str__()

    # get a derivative of the formula
    def get_derivative(self):

        args = []
        i = len(self.coefs)
        for coef in self.coefs:
            i -= 1
            args.append(i * coef)

        args = args[:-1]

        return F(*args)

    # return the formula's degree
    def degree(self):
        return len(self.coefs) - 1

    # solve the formula
    def solve(self):

        result = []

        if (self.degree() == 1):
            x = lambda a, b: (-1 * b / a)

            result.append(x(*self.coefs))

        if (self.degree() == 2):
            d = lambda a, b, c: (b**2 - 4*a*c)
            x = lambda s, a, b, c: (-1*b + (-1)**s *
                                    sqrt( d(a,b,c) )) / (2*a)

            result.append(x(0, *self.coefs))
            result.append(x(1, *self.coefs))

        if (self.degree() >= 3):
            raise NotImplementedError()

        return result


print "please input 4 numbers (a-d, each number must be separated by RETURN):"

f = F(input(), input(), input(), input()) # make an instance of F with 4 numbers
f_d = f.get_derivative()                  # get a derivative

# show
print "f(x) =" + str(f)
print "f'(x) =" + str(f_d)

# solve the derivative
solutions = f_d.solve()

# get, sort values
values = [(x, f[x]) for x in solutions]
values.sort(key = lambda v: v[1].real)
values.sort(key = lambda v: v[1].imag)

print "min: f(%s) = %s" % (str(values[0][0]), str(values[0][1]))
print "max: f(%s) = %s" % (str(values[1][0]), str(values[1][1]))
