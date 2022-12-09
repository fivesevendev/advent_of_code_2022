#AOC-2022-8-1


import timeit
import time


def numFind(n):
    global f
    vis = {}
    with open("8.txt") as f:
        f = f.read()
    f = [list(map(int, list(s))) for s in f.split("\n")]
    rLen = len(f)
    cLen = len(f[0])
    
    #build the dict w/all locations False except perimeters
    for a in range(rLen):
        for b in range(cLen):
            if a == 0 or a == rLen - 1 or b == 0 or b == cLen - 1:
                vis[(a, b)] = True
            else:
                vis[(a, b)] = False

    #one loop w/4 checks that break the loop
    for x in range(1, rLen - 1):
        for y in range(1, cLen - 1):
            height = f[x][y]
            if vis[(x, y)] == False:
                if fromBottom(height, x, y, rLen) or fromLeft(height, x, y, cLen) or fromRight(height, x, y, cLen) or fromTop(height, x, y, rLen):
                    vis[(x, y)] = True
                
    #prints visible representation of the grid
#    for rr in range(rLen):
#        for cc in range(cLen):
#            print(vis[(rr, cc)], end=",   ")
#        print("\n")
    ##########################################
    return list(vis.values()).count(True)

def fromBottom(h, x, y, rL):
    for q in range(rL - 1, x, -1):
        if f[q][y] >= h:
            return False
    return True

def fromLeft(h, x, y, cL):
    for q in range(0, y, 1):
        if f[x][q] >= h:
            return False
    return True

def fromRight(h, x, y, cL):
    for q in range(cL - 1, y, -1):
        if f[x][q] >= h:
            return False
    return True

def fromTop(h, x, y, rL):
    for q in range(0, x, 1):
        if f[q][y] >= h:
            return False
    return True


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")