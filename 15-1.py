#AOC-2022-15-1


import timeit
import time


grid = {}


def numFind(y):
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
    
    for ff in f:
        width = 0
        sensorCenter = (ff[1], ff[0])
        beacon = (ff[3], ff[2])
        grid[sensorCenter] = "S"
        grid[beacon] = "B"
        mD = manhat(sensorCenter, beacon)
        while width <= mD:
            if ff[1] - (mD - width) == y: #checks if its the one row we care about
                for c in range(ff[0] - width, ff[0] + width + 1): #starts top peak of diamond going thru base
                    if (ff[1] - (mD - width), c) not in grid:  #makes sure nothing else at that position
                        grid[(ff[1] - (mD - width), c)] = "#"
            width += 1
        width -= 2
        while width >= 0:
            if ff[1] + (mD - width) == y: #checks if its the one row we care about
                for c in range(ff[0] - width, ff[0] + width + 1): #starts line under base thru bottom peak
                    if (ff[1] + (mD - width), c) not in grid: #makes sure nothing else at that position
                        grid[(ff[1] + (mD - width), c)] = "#"
            width -= 1
    return len([g for g in grid if g[0] == y and grid[g] == '#'])

def manhat(a, b):
    aa = abs(a[0] - b[0])
    bb = abs(a[1] - b[1])
    return aa + bb


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    y = 2000000
    print("Result:", numFind(y))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")