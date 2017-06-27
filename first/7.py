#!/usr/bin/python

import itertools
import sys

print "please input numbers(1~9, each number must be separated by SPACE):"

pool = map(int, raw_input().split())

for tup in list(itertools.combinations(pool, 2)):
    if tup[0] == tup[1]:
        print "invalid input number(duplicated)"
        sys.exit(1)

count = 0
for number in list(itertools.permutations(pool)):
    print number
    count += 1

print "total: %d number(s)" % count
