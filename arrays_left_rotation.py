# HackerRank 'Arrays: Left Rotation' solution - Python 3
# https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotLeft(a, d):
    for i in range(d):
        elem = a[0]
        a.pop(0)
        a.append(elem)
    return a


rotLeft([1, 2, 3, 4, 5], 2)
