#!/usr/bin/env python3
import re

workflows, starts = open("../inputs/day19").read().split('\n\n')

rules = {}
for wf in workflows.split('\n'):
    name, wf = wf.split('{')
    rules[name] = wf.strip('}')

t = 0
for start in starts.split('\n')[:-1]:
    x,m,a,s = map(int, re.findall(r"\d+", start))
    
    rule = "in"
    while rule not in "AR":
        if rule in rules:
            rule = rules[rule]

        cond, rule = rule.split(':', 1)
        if eval(cond):
            rule,_ = rule.split(',', 1)
        else:
            _,rule = rule.split(',', 1)
    if rule == 'A':
        t += x + m + a + s
# print(t)


from collections import deque

wfs = deque([("in", ((0, 4000), (0, 4000), (0, 4000), (0, 4000)))])

while wfs:
    rule, (x, m, a, s) = wfs.popleft()
    if rule in rules:
        rule = rules[rule]
    
    cond, rule = rule.split(':', 1)
    if '>' in cond:
        val = int(cond[2:].split(':')[0])
        print(val)
    if '<' in cond:
        val = int(cond[2:].split(':')[0])
        branch_true, branch_false = rule.split(',', 1)
        if cond[0] == 'x':
            if x[0] < val:
                wfs.append((branch_true, ((x[0], val - 1), m, a, s)))
            if x[1] >= val:
                wfs.append((branch_false, ((val, x[1]), m, a, s)))
        if cond[0] == 'm':
            if m[0] < val:
                wfs.append((branch_true, (x, (m[0], val - 1), a, s)))
            if m[1] >= val:
                wfs.append((branch_false, (x, (val, m[1]), a, s)))
        if cond[0] == 'a':
            if a[0] < val:
                wfs.append((branch_true, (x, m, (a[0], val - 1), s)))
            if a[1] >= val:
                wfs.append((branch_false, (x, m, (val, a[1]), s)))
        if cond[0] == 's':
            if s[0] < val:
                wfs.append((branch_true, (x, m, a, (s[0], val - 1))))
            if s[1] >= val:
                wfs.append((branch_false, (x, m, a, (val, s[1]))))
print(wfs)
