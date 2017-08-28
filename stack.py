#!/usr/bin/env python

lst = [1,2,3,4,5,]

def push(x):
    lst.append(x)

def pop():
    return lst.pop()

push(6)
push(7)
push(8)
print pop()
print pop()
print pop()
