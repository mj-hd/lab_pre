#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

# 投票数をnとし、候補者数をmとすると、

# 辞書構造に二分探索木を用いているため、
# 候補者のノード数 m により計算量が決まる。
# 挿入・検索処理に関して計算量はO(log2(m))

# また、投票全体を走査し、カウントアップ(挿入・検索)していくため、
# 計算量はO(n log2(m))

# よって、
# 集計処理全体はO(n log2(m))である

# m <= nであるとすると、
# 計算量はO(n^2)よりも少ない

# 木構造のノードを表すクラス
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.children = [left, right]
        self.value = value

    # 値を取得する
    def get(self):
        return self.value

    # 値を設定する
    def set(self, v):
        self.value = v

    # 子供を取得する
    def __getitem__(self, i):
        if i > 1:
            raise IndexError()
        return self.children[i]

    # 子供を設定する
    def __setitem__(self, i, v):
        if i > 1:
            raise IndexError()
        self.children[i] = v

    # 左に子供を持つか
    def has_left(self):
        return self.children[0] != None

    # 右に子供を持つか
    def has_right(self):
        return self.children[1] != None

    # 左の子供を取得する
    def get_left(self):
        return self.children[0]

    # 右の子供を取得する
    def get_right(self):
        return self.children[1]

    # 左の子供を設定する
    def set_left(self, left):
        self.children[0] = left

    # 右の子供を設定する
    def set_right(self, right):
        self.children[1] = right

    # 文字列へ変換する
    def __repr__(self):
        return "* " + str(self.value) + " L:{" + str(self.children[0]) + "}, R:{" + str(self.children[1]) + "}"

# 辞書の値を表すクラス
class DictionaryValue:
    def __init__(self, _hash, key, value):
        self.hash = _hash  # キーのハッシュ値
        self.key = key     # キー
        self.value = value # 値

    # ハッシュ値を取得する
    def get_hash(self):
        return self.hash

    # キーを取得する
    def get_key(self):
        return self.key

    # 値を取得する
    def get_value(self):
        return self.value

    # ハッシュ値を設定する
    def set_hash(self, _hash):
        self.hash = _hash

    # キーを設定する
    def set_key(self, key):
        self.key = key

    # 値を設定する
    def set_value(self, value):
        self.value = value

    # ハッシュ値を返す
    def __int__(self):
        return int(self.hash)

    # 文字列へ変換する
    def __repr__(self):
        return "[" + str(self.key) + "(" + str(self.hash) + ")," + str(self.value) + "]"

# 二分探索木を表すクラス
class BinarySearchTree:
    def __init__(self):
        self.root = Node() # ルートを作成

    # キーについて探索をする
    # 理想: log2(n)
    def find(self, key):
        n = self.root
        while n != None and n.get() != None: # 終端でない間
            if int(n.get()) > key: # キーが小さければ左を調べる
                n = n.get_left()
            elif int(n.get()) < key: # キーが大きければ右を調べる
                n = n.get_right()
            else: # 等しければ結果を返す
                break

        return n

    # 値を木に追加する
    def insert(self, value):
        n = self.root
        p = None
        # 追加する場所を決定する
        while n != None and n.get() != None: # 終端でない間
            p = n # 直前のノードを取っておく
            if int(p.get()) > int(value):
                n = n.get_left()
            else:
                n = n.get_right()

        # ルートしか木に存在しない場合
        if p == None or p.get() == None:
            self.root.set(value)
            return

        # 新しくノードを作成し、設定する
        n = Node(value)
        if int(p.get()) > int(value):
            p.set_left(n)
        else:
            p.set_right(n)

    # 巡回するイテレータ
    def each_in_order(self, n = None):
        if n == None:
            n = self.root

        yield n
        if n.has_left():
            yield from self.each_in_order(n.get_left())
        if n.has_right():
            yield from self.each_in_order(n.get_right())

    # 文字列へ変換する
    def __repr__(self):
        return str(self.root)

# 辞書を表すクラス
class Dictionary:
    def __init__(self):
        self.tree = BinarySearchTree() # 木として二分探索木を使用する
        self.hash = lambda x:(hash(x)) # ハッシュ関数としてhashを使用する

    # 要素を取り出す
    def __getitem__(self, key):
        _hash = self.hash(key)      # ハッシュ値を計算し
        val = self.tree.find(_hash) # 探索し
        if val == None or val.get() == None:
            return None
        return val.get().get_value() # 返す

    # 要素を設定する
    def __setitem__(self, key, value):
        _hash = self.hash(key)       # ハッシュ値を計算し
        cand = self.tree.find(_hash) # 探索し
        if cand != None and cand.get() != None: # キーが存在すれば
            cand.get().set_value(value) # 値を更新し
        else:                           # 存在しなければ
            self.tree.insert(DictionaryValue(_hash, key, value)) # ノードを追加する

    # キーが存在するかどうか
    def has_key(self, key):
        _hash = self.hash(key)
        val = self.tree.find(_hash)
        return val != None and val.get() != None

    # キーが存在するかどうか(Python3の構文用)
    def __contains__(self, key):
        return self.has_key(key)

    # 値を巡回する
    def iteritems(self):
        for item in self.tree.each_in_order():
            yield (item.get().get_key(), item.get().get_value())

    # 値を巡回する(Python3の構文用) 若干遅い
    def items(self):
        result = []
        for item in self.iteritems():
            result.append(item)

        return result

    # 文字列へ変換する
    def __repr__(self):
        return str(self.tree)

# それぞれの行について処理を行う
for line in open("list.txt", "r"):
    count = Dictionary() # 辞書を作成する
    #count = {}
    length = 0 # 文字列のながさ

    # それぞれの文字について走査
    # 計算量: n log(m)
    # n: 投票数
    # m: 候補者数
    for char in list(line.rstrip()):
        if not(char in count): # キーが辞書に存在しなければ
            count[char] = 0    # 0として初期化

        count[char] += 1 # カウントアップ
        length += 1      # カウントアップ

    # 最も投票数の多かった候補と、その数を取得する
    # 計算量: m
    # m: 候補者数
    cand, votes = max(count.items(), key=lambda x:x[1])

    # 結果を出力する
    print(line, end="")
    if votes >= (length + 1) / 2: # 過半数であるかどうかの判定
        print(" => " + cand)
    else:
        print(" => revote!")


