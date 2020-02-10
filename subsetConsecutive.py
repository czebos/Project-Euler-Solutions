#!/usr/bin/python

#https://projecteuler.net/problem=93

d = {}
tag = {}
max = 0

def joinNumber(n1,n2):
    list = []
    list.append(n1-n2)
    list.append(n2-n1)
    list.append(n1+n2)
    list.append(n1*n2)
    if(n2 != 0):
        list.append(n1/n2)
    if(n1 != 0):
        list.append(n2/n1)
    return list

def findNumbers(list):
    if len(list) > 2:
        for i in range(len(list)):
            for j in range(len(list) - 1 - i):
                possible = joinNumber(list[i], list[j+1 + i])
                copy = list.copy()
                copy.remove(list[i])
                copy.remove(list[j+1 + i])
                for pos in possible:
                    copy.append(pos)
                    findNumbers(copy)
                    copy.pop()
    else:
        secondl = joinNumber(list[0], list[1])
        for pos in secondl:
            d[pos] = True

answer = ""
for i in range(7):
    for j in range(8):
        for k in range(9):
            for l in range(10):
                list = []
                d = {}
                if(i< j and j< k and k< l):
                    list.append(i)
                    list.append(j)
                    list.append(k)
                    list.append(l)
                    findNumbers(list)
                    print(str(i) + str(j) + str(k) + str(l))
                    p = 1
                    while p in d:
                        print(p)
                        p += 1
                    if p > max:
                        max = p
                        answer = (str(i) + str(j) + str(k) + str(l))
print(max)
print(answer)
