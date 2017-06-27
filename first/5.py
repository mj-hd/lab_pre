#!/usr/bin/python

import itertools

class Map:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.map = [[0 for y in range(h)] for x in range(w)]

    def __getitem__(self, p):
        x, y = p
        if x >= self.width or y >= self.height or x < 0 or y < 0:
            raise IndexError()

        return self.map[x][y]

    def __setitem__(self, p, v):
        x, y = p
        if x >= self.width or y >= self.height or x < 0 or y < 0:
            raise IndexError()

        self.map[x][y] = v

    def __str__(self):
        result = ""

        for y in range(0, self.height):
            for x in range(0, self.width):
                result += "%d " % self[x, y]
            result += "\n"

        return result

    def __repr__(self):
        return self.__str__()

    def parse(self, source):
        x = 0
        y = 0
        for c in source:
            if c == "\n":
                x  = 0
                y += 1
                continue

            self[x, y] = int(c)
            x += 1

class Route:
    def __init__(self, source):
        self.source = source

    def __str__(self):
        result = ""
        for c in self.source:
            if c == 0:
                result += "Right "
            else:
                result += "Down "

        return result 

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, i):
        return self.source[i]

    def hash(self):
        result = 0
        i = 0
        for s in self.source:
            result += s * 2**i
            i += 1

        return result

    def sum(self):
        result = 0
        for s in self.source:
            result += s

        return result


h, w = map(int, raw_input().split())

if not(2 <= h and h <= 50):
    raise Exception("invalid height")
if not(2 <= w and w <= 50):
    raise Exception("invalid weight")

m = Map(w, h)

source = ""
for y in range(0, h):
    source += raw_input() + "\n"

m.parse(source)

print "map:"
print m

digits = m.width + m.height - 2
min_semi = 9*digits
min_r = None
for attempt in list(itertools.product((0, 1), repeat=digits)):
    r = Route(attempt)
    if r.sum() != h - 1:
        continue

    x = 0
    y = 0
    semi = m[0, 0]
    for d in r.source:
        if d == 0:
            x += 1
        else:
            y += 1

        semi += m[x, y]

    if min_semi > semi:
        min_semi = semi
        min_r = r

print min_r
print "Semi: " + str(min_semi)
