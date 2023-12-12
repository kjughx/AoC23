#!/bin/env python3
import math # factorial
import re

lines = [line.strip() for line in open("../inputs/day12").readlines()]


def f(l, s, i, gi, c):
    print(l, s, i, gi, c)
    if i == len(l):
        if gi != len(s):
            return 0
        else:
            return 1

    if l[i] == '.':
        if c > 0:  # end of group
            return f(l, s, i + 1, gi + 1, 0)
        return f(l, s, i + 1, gi, 0)

    if l[i] == '#':
        if c < s[gi]:
            return f(l, s, i + 1, gi, c + 1)
        return 0

    # Try both '.' and '#'
    l[i] = '1'
    dots = f(l, s, i + 1, gi + (1 if c else 0), False)

    l[i] = '2'
    hashes = 0
    if c < s[gi]:
        hashes = f(l, s, i + 1, gi, c + 1)


    return dots + hashes

    # return f(l, s, i + 1, gi + (1 if g else 0), False) + f(l, s, i + 1, gi, True)


t = 0
for line in [lines[0]]:
    springs, sizes = line.split(" ")
    sizes = list(map(int, sizes.split(",")))
    t += f(list(springs), sizes, 0, 0, False)
print(t)
