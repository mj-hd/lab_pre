#!/usr/bin/python
# -*- coding: utf-8 -*-

print "駄菓子の数:",
count = input()
print "予算の上限:",
money = input()

snacks = []
print "(値段 満足度)"
for i in range(0, count):
    print str(i) + ":",
    tmp = raw_input().split(' ')
    snacks.append((i, int(tmp[0]), int(tmp[1])))


print "(1)貪欲法:"
values = [(i, float(snacks[i][2]) / float(snacks[i][1])) for i in range(0, count)]
bag = []
cost = 0
sast = 0
while(True):
    if len(values) == 0:
        break

    top = max(values, key=lambda x:x[1])
    cost += snacks[top[0]][1]

    if cost >= money:
        break

    sast += snacks[top[0]][2]
    bag.append(snacks[top[0]])
    values.remove(top)

print "最大満足度:" + str(sast)
print "番号 値段 満足度"
for snack in bag:
    print str(snack[0]) + " " + str(snack[1]) + " " + str(snack[2])


#print "(2)深さ優先探索:"
#bag = []
#cost = 0
#sast = 0
#
#
#
#print "最大満足度:" + str(sast)
#print "番号 値段 満足度"
#for snack in bag:
#    print str(snack[0]) + " " + str(snack[1]) + " " + str(snack[2])
#
#
