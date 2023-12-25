#!/usr/bin/env python3
import numpy as np

lines = [line.strip() for line in open("../inputs/day18").readlines()]

loop = []
for line in lines:
    d, l, color = line.split(' ')

    l = int(l)
    if d == 'R':
        r,c = r, c + l
    elif d == 'L':
        r,c = r, c - l
    elif d == 'D':
        r,c = r + l, c
    elif d == 'U':
        r, c = r - l ,c

    loop.append((r, c, color))

rs = set()
for i, (r,c, _) in enumerate(loop):

print(t + 1)
