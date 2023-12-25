#!/usr/bin/env python3
# part 1 done somewhere else
from collections import deque

import numpy as np

lines = np.array([[c for c in line.strip()] for line in open('../inputs/day14').readlines()])
R = lines.shape[0]
C = lines.shape[1]

os = list(zip(np.where(lines == 'O')[0], np.where(lines == 'O')[1]))
hs = list(zip(np.where(lines == '#')[0], np.where(lines == '#')[1]))

def roll(dr, dc, new):
    roll = True
    while roll:
        old = new
        new = []
        roll = False
        for r,c in old:
            nr,nc = r + dr, c + dc
            if lines[nr, nc] == '.' and 0 <= nr < R and 0 <= nc < C:
                new.append((nr, nc))
                roll = True
        for r,c in new:
            lines[nr, nc] = 'O'
            lines[r, c] = '.'

    return new


new = roll(-1, 0, os)
print(lines)

