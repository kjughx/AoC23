#!/usr/bin/env python3
import numpy as np

grid = np.array([[c for c in line.strip()] for line in open('../inputs/day21').readlines()])
R = grid.shape[0]
C = grid.shape[1]

start = tuple(map(int, (np.where(grid == 'S')[0][0], np.where(grid == 'S')[1][0])))

steps = {start}
steps = 0
for step in range(100):
    new = set()
    for r,c in steps:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if grid[(r + dr) % R , (c + dc) % C] == '.':
                new.add((r + dr, c + dc))
    steps = new
print(len(steps) + 1)
