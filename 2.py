#!/usr/bin/python

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def is_prime(n):
    MAX_A = 10     # attempt a up to
    prime = lambda a, n: a**(n-1) % n == 1 # prime condition

    for a in range(2, MAX_A):
        if gcd(a, n) != 1: # not disjoint
            continue

        if not(prime(a, n)):
            return False

    return True

print "please input a number:"
n = input()

result = "%d is " % n
if is_prime(n):
    result += "prime"
else:
    result += "not prime"

print result
