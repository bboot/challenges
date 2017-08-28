#!/usr/bin/env python2

def findClosestElements(arr, k, x):
    b = sorted((abs(x - t), t) for t in arr)
    sol = sorted(map(lambda t: t[1], b[0:k]))
    return sol

def findClosestElements2(A, K, X):
    A.sort(key = lambda x: (abs(x-X), x))
    return sorted(A[:K])

arr = [1, 2, 3, 100, 101, 102]
k = 4
x = 100

ans = findClosestElements(arr, k, x)
ans = findClosestElements2(arr, k, x)
print ans
