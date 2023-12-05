#!/bin/env python3

maps = [{} for _ in range(7)]

lines = [line.strip('\n') for line in open("../inputs/day5").readlines()]
seeds = list(map(int, lines[0].split(": ")[1].split(" ")))

id=0
for line in lines[2::]:
    if len(line) == 0:
        id += 1
        continue
    elif line[0].isalpha():
        continue
    dst,src,r = map(int, line.split(" "))
    maps[id][src] = (dst, r)

locations = []
for seed in seeds:
    found = True
    for i, m in enumerate(maps):
        for (src, (dst, r)) in m.items():
            if seed < src or seed >= src + r:
                continue
            if src <= seed < src + r - 1:
                seed = seed - src + dst
                found = True
                break

    locations.append(seed)
print(min(locations))

seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(len(seeds)-1)]
# split ranges into posssibly three ranges
mins = []
for m in maps:
    mseeds = []
    for (src, (dst, r)) in m.items():
        nseeds = []
        while (len(seeds) > 0):
            ss, se = seeds.pop()
            # how to find seeds in [src, src + r]?
            # the seed range in the source range: [srs, sre)
            srs = max(ss, src)
            sre = min(src + r, se)

            if ss < src: # before source
                nseeds.append((ss, src))
            if se >= src + r: # after source
                nseeds.append((src+r, se))

            if srs < sre: # then there are seeds in the source range
                mseeds.append((dst + (srs - src), dst + (sre - src)))
        seeds = nseeds
    seeds = seeds + mseeds
    mins.append(min(seeds)[0])
    print(mins)
print(min(mins))

