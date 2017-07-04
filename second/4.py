#!/usr/bin/python3
import sys

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.children = [left, right]
        self.value = value

    def get(self):
        return self.value

    def set(self, v):
        self.value = v

    def __getitem__(self, i):
        if i > 1:
            raise IndexError()
        return self.children[i]

    def __setitem__(self, i, v):
        if i > 1:
            raise IndexError()
        self.children[i] = v

    def has_left(self):
        return self.children[0] != None

    def has_right(self):
        return self.children[1] != None

    def get_left(self):
        return self.children[0]

    def get_right(self):
        return self.children[1]

    def set_left(self, left):
        self.children[0] = left

    def set_right(self, right):
        self.children[1] = right

    def __repr__(self):
        return "* " + str(self.value) + " L:{" + str(self.children[0]) + "}, R:{" + str(self.children[1]) + "}"

class DictionaryValue:
    def __init__(self, _hash, key, value):
        self.hash = _hash
        self.key = key
        self.value = value

    def get_hash(self):
        return self.hash

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_hash(self, _hash):
        self.hash = _hash

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def __int__(self):
        return int(self.hash)

    def __repr__(self):
        return "[" + str(self.key) + "(" + str(self.hash) + ")," + str(self.value) + "]"

class BinarySearchTree:
    def __init__(self):
        self.root = Node()

    def find(self, key):
        n = self.root
        while n != None and n.get() != None:
            if int(n.get()) > key:
                n = n.get_left()
            elif int(n.get()) < key:
                n = n.get_right()
            else:
                break

        return n

    def insert(self, value):
        n = self.root
        p = None
        while n != None and n.get() != None:
            p = n
            if int(p.get()) > int(value):
                n = n.get_left()
            else:
                n = n.get_right()

        if p == None or p.get() == None:
            self.root.set(value)
            return

        n = Node(value)
        if int(p.get()) > int(value):
            p.set_left(n)
        else:
            p.set_right(n)

    def each_in_order(self, n = None):
        if n == None:
            n = self.root

        yield n
        if n.has_left():
            yield from self.each_in_order(n.get_left())
        if n.has_right():
            yield from self.each_in_order(n.get_right())

    def __repr__(self):
        return str(self.root)


class Dictionary:
    def __init__(self):
        self.tree = BinarySearchTree()
        self.hash = lambda x:(hash(x))

    def __getitem__(self, key):
        _hash = self.hash(key)
        val = self.tree.find(_hash)
        if val == None or val.get() == None:
            return None
        return val.get().get_value()

    def __setitem__(self, key, value):
        _hash = self.hash(key)
        cand = self.tree.find(_hash)
        if cand != None and cand.get() != None:
            cand.get().set_value(value)
        else:
            self.tree.insert(DictionaryValue(_hash, key, value))

    def has_key(self, key):
        _hash = self.hash(key)
        val = self.tree.find(_hash)
        return val != None and val.get() != None

    def __contains__(self, key):
        return self.has_key(key)

    def iteritems(self):
        for item in self.tree.each_in_order():
            yield (item.get().get_key(), item.get().get_value())

    def items(self):
        result = []
        for item in self.iteritems():
            result.append(item)

        return result

    def __repr__(self):
        return str(self.tree)

for line in open("list.txt", "r"):
    count = Dictionary()
    #count = {}
    length = 0
    for char in list(line.rstrip()):
        if not(char in count):
            count[char] = 0

        count[char] += 1
        length += 1

    cand, votes = max(count.items(), key=lambda x:x[1])

    print(line, end="")
    if votes >= (length + 1) / 2:
        print(" => " + cand)
    else:
        print(" => revote!")


