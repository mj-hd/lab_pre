#!/usr/bin/python
# -*- coding: utf-8 -*-

# 最大公約数を求める関数
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

# 素数であるかどうかを返す関数
def is_prime(n):
    MAX_A = 10     # 試行するaの最大値
    prime = lambda a, n: a**(n-1) % n == 1 # 素数である条件

    for a in range(2, MAX_A):
        if gcd(a, n) != 1: # 素数でない場合
            continue

        if not(prime(a, n)):
            return False

    return True

print "値を入力してください:"
n = input()

# 最も近い素数の距離
closest_i_pos = 1 # 正
closest_i_neg = 1 # 負

# 探す
while(not(is_prime(n + closest_i_pos))):
    closest_i_pos += 1

while(not(is_prime(n - closest_i_neg))):
    closest_i_neg += 1

# 負の方面に不正な値をとった場合、結果から除外する
if (n - closest_i_neg <= 1):
    closest_i_neg = float('inf')

# 出力処理
result = ""
if closest_i_neg <= closest_i_pos:
    result += str(n - closest_i_neg)

if closest_i_pos == closest_i_neg:
    result += ","

if closest_i_pos <= closest_i_neg:
    result += str(n + closest_i_pos)

print result
