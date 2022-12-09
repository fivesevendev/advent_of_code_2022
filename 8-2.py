#AOC-2022-8-2


import timeit
import time
from math import prod

def numFind(n):
    global f
    vis = {}
    with open("8.txt") as f:
        f = f.read()
    f = [list(map(int, list(s))) for s in f.split("\n")]
    rLen = len(f)
    cLen = len(f[0])
    
    #build the dict w/all locations 0
    for a in range(rLen):
        for b in range(cLen):
            vis[(a, b)] = 0

    #one loop w/4 direction checks
    for x in range(0, rLen):
        for y in range(0, cLen):
            height = f[x][y]
            vis[(x, y)] = prod([toBottom(height, x, y, rLen), toLeft(height, x, y, cLen), toRight(height, x, y, cLen), toTop(height, x, y, rLen)])

    #prints visible representation of the grid
#    for rr in range(rLen):
#        for cc in range(cLen):
#            print(vis[(rr, cc)], end=",   ")
#        print("\n")
    ##########################################
    return max(vis.values())

def toBottom(h, x, y, rL):
    c = 1
    for q in range(x + 1, rL, 1):
        if f[q][y] < h:
            c += 1
        else:
            return c
    return c - 1

def toLeft(h, x, y, cL):
    c = 1
    for q in range(y - 1, -1, -1):
        if f[x][q] < h:
            c += 1
        else:
            return c
    return c - 1

def toRight(h, x, y, cL):
    c = 1
    for q in range(y + 1, cL, 1):
        if f[x][q] < h:
            c += 1
        else:
            return c
    return c - 1

def toTop(h, x, y, rL):
    c = 1
    for q in range(x - 1, -1, -1):
        if f[q][y] < h:
            c += 1
        else:
            return c
    return c - 1


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")