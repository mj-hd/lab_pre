#!/usr/bin/python

class Line:
    def __init__(self, startx, starty, endx, endy):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy

        self.d = float(endy - starty) / float(endx - startx)

    def intersects(self, line):
        return line.d != self.d

print "please input first line(startx, starty, endx, endy, separated by RETURN):"
l1 = Line(input(), input(), input(), input())

print "please input second line(startx, starty, endx, endy, separated by RETURN):"
l2 = Line(input(), input(), input(), input())

if l1.intersects(l2):
    print "l1 intersects l2"
else:
    print "l1 does not intersect l2"
