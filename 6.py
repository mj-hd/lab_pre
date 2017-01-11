#!/usr/bin/python

import random
import math
import itertools

def norm(a):
    return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def angle(a, b):
    if dot(a,b) == 0:
        return math.pi / 2.0
    return math.acos(dot(a, b) / (norm(a) * norm(b)))

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

class Pyramid:
    def __init__(self, x, y, h):
        self.x = float(x)
        self.y = float(y)
        self.h = float(h)

        self.polygon  = [(0,0,0), (self.x,0,0), (self.x,self.y,0), (0, self.y, 0), (1.0/2.0*self.x, 1.0/2.0*self.y, self.h)]
        #self.polygon = [(0,0,0), (self.x*1.0/3.0,0,0), (self.x*1.0/3.0,self.y,0), (0, self.y, 0), (0,0,self.h), (self.x*1.0/3.0,0,self.h), (self.x*1.0/3.0,self.y,self.h), (0, self.y, self.h)]

    def contains(self, x, y, z):
        # target
        t = (x, y, z)

        # origin
        for o in self.polygon:
            d = sub(t, o) # o -> t

            # target = o + d*1.0

            # select 3 vectors exclusive of origin
            for trig in itertools.combinations([p for p in self.polygon if p != o], 3):
                v0 = sub(trig[0], o)
                v1 = sub(trig[1], o)
                v2 = sub(trig[2], o)
                e1 = sub(v1, v0) # v0 -> v1
                e2 = sub(v2, v0) # v0 -> v2
                r  = sub(o,  v0) # v0 -> o

                u = cross(d, e2)
                v = cross(r, e1)

                unit = 1.0/dot(u, sub(v1, v2))

                time = unit * dot(v, e2)
                b    = unit * dot(u, r)
                c    = unit * dot(v, d)

                # print str(t) + ", TIME: " + str(time) + ", B:" + str(b) + ", C:" + str(c) + ", B+C:" + str(b + c)
                if time <= 1 and b + c < 1 and b > 0 and c > 0:
                    return False

        print t
        return True

pyramid = Pyramid(input(), input(), input())

print "calculating..."

# calculate volume of pyramid with Monte Carlo
times = 1000

count = 0
for i in range(times):
    x = random.random() * pyramid.x
    y = random.random() * pyramid.y
    h = random.random() * pyramid.h

    if pyramid.contains(x, y, h):
        count += 1

p = (float(count) / float(times))

print(p) # should be 1/3

v = p * pyramid.x * pyramid.y * pyramid.h

print(v)

print("correct answer:" + str(1.0/3.0 * pyramid.x * pyramid.y * pyramid.h))


#while True:
#    print(pyramid.contains(float(input()), float(input()), float(input())))
