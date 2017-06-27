#!/usr/bin/python

import binarytree

def preorder_print(tree):
    result = str(tree.value) + " "
    if tree.left != None:
        result += preorder_print(tree.left)
    if tree.right != None:
        result += preorder_print(tree.right)
    return result

def inorder_print(tree):
    result = ""
    if tree.left != None:
        result += inorder_print(tree.left)
    result += str(tree.value) + " "
    if tree.right != None:
        result += inorder_print(tree.right)
    return result

def postorder_print(tree):
    result = ""
    if tree.left != None:
        result += postorder_print(tree.left)
    if tree.right != None:
        result += postorder_print(tree.right)
    result += str(tree.value) + " "
    return result

l = [4,7,9,13,8,10,22,6,15,3,18,30,11,1,29]

i = 0
s = 1
while s <= len(l):
    if s == len(l):
        break
    i += 1
    s += 2**i

if 2**i + 1 > len(l):
    raise Exception("invalid list")

t = binarytree.convert(l)

binarytree.pprint(t)

print "preorder:" + preorder_print(t)

print "inorder:" + inorder_print(t)

print "postorder:" + postorder_print(t)
