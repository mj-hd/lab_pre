#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import floor, sqrt, hypot

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

# 値から座標を求める関数
def get_position(n):
    prev_level = floor(sqrt(n - 0.1))
    level = prev_level + 1
    return (int(level - (max((n - prev_level ** 2) - level, 0))), int(min(n - prev_level ** 2, level)))

# 座標から値を求める関数
def get_value(x, y):
    if x <= 0 or y <= 0:
        return -1
    if x <= y:
        prev_level = y - 1
    if y < x:
        prev_level = x - 1
    return int(prev_level ** 2 + y + max(y - x, 0))

# 入力された値と、その座標を得る
print "値を入力してください:"
n = input()
n_pos = get_position(n)

found = False # 素数が見つかったフラグ
result = []   # 最も近い素数の一覧
distance = 0  # 現在探索している深さ

while(not(found)):
    # 初期化
    result = []
    distance += 1

    # 周囲のマス全てについて
    line = distance * 2 + 1
    half = int(line / 2)
    for i in range(0, line ** 2):
        # 試行する座標と、その値を得る
        diff_x = i % line - half
        diff_y = i / line - half
        attempt = (n_pos[0] + diff_x, n_pos[1] + diff_y)

        # 周囲のみを探索する
        if not(abs(diff_x) == half or abs(diff_y) == half):
            continue

        # 座標に対応する値を取得する
        value = get_value(*attempt)

        # 不正な値ならcontinue
        if value <= 0:
            continue

        # 素数であれば、結果にその値と距離を代入し、フラグをセット
        if is_prime(value):
            result.append((value, hypot(n_pos[0] - attempt[0], n_pos[1] - attempt[1])))
            found = True

# 最も距離の小さなものを取り出し、同じ距離の要素を全て取り出す
closest_dist = min([item[1] for item in result])
closest_items = [item[0] for item in result if item[1] == closest_dist]

# 結果を出力
print closest_items
