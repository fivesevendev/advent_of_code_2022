#AOC-2022-15-2


import timeit
import time
import sys

grid = []


def numFind(mx):
    with open("15.txt") as f:
        f = f.read()
    f = [s for s in f.split("\n")]
    for line in range(len(f)):
        f[line] = str(f[line]).replace("Sensor at x=", "")
        f[line] = str(f[line]).replace(" y=", "")
        f[line] = str(f[line]).replace(":", ",")
        f[line] = str(f[line]).replace(" closest beacon is at x=", "")
        f[line] = str(f[line]).replace(" y=", "")
        f[line] = list(map(int, f[line].split(",")))
    progress = 1
    for ff in f:
        print("Progress:", progress)
        kill = []
        width = 0
        sensorCenter = [ff[1], ff[0]]
        beacon = [ff[3], ff[2]]
        grid.append(sensorCenter)
        grid.append(beacon)
        mD = manhat(sensorCenter, beacon)
        grid.append([ff[1] - 1, ff[0]]) #sets exclusion one row higher than peak
        while width <= mD:            
            r = ff[1] - (mD - width)
            grid.append([r, ff[0] - width - 1]) #set a point left side of boundary
            grid.append([r, ff[0] + width + 1]) #set a point right side of boundary
            for check in grid:
                if (ff[0] - width - 1) < check[1] < (ff[0] + width + 1):
                    kill.append(check)
            width += 1
        width -= 2
        while width >= 0:
            r = ff[1] + (mD - width)
            grid.append([r, ff[0] - width - 1]) #set a point left side of boundary
            grid.append([r, ff[0] + width + 1]) #set a point right side of boundary
            for check in grid:
                #print("check:", check, "r:", r)
                if (ff[0] - width - 1) < check[1] < (ff[0] + width + 1):
                    kill.append(check)
            width -= 1
        grid.append([ff[1] + 1, ff[0]]) #sets exclusion one row lower than peak
        #print("old:", sorted(grid))
        #print()
        #print("kill:", sorted(kill))
        #print()
        for k in kill:
            if k in grid:
                grid.remove(k)
        #print("new", sorted(grid))
        #break
        #sys.exit()
        progress += 1
    for q in grid:
        if 0 <= q[0] <= mx and 0 <= q[1] <= mx:
            print(q, end=", ")
    print()
    print("len:", len(grid))

def manhat(a, b):
    aa = abs(a[0] - b[0])
    bb = abs(a[1] - b[1])
    return aa + bb
    

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    mx = 20
    print("Result:", numFind(mx))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")