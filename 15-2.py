#AOC-2022-15-2


import timeit
import time


grid = {}


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
        print("Line: ", progress)
        width = 0
        sensorCenter = (ff[1], ff[0])
        beacon = (ff[3], ff[2])
        grid[sensorCenter] = "S"
        grid[beacon] = "B"
        mD = manhat(sensorCenter, beacon)
        while width <= mD:            
            r = ff[1] - (mD - width)
            for c in range(ff[0] - width, ff[0] + width + 1): #starts top peak of diamond going thru base
                if c > mx or c < 0 or r > mx or r < 0: #checks if its too big or too small for area of concern
                    continue
                grid[(r, c)] = None
            width += 1
        width -= 2
        while width >= 0:
            r = ff[1] + (mD - width)
            for c in range(ff[0] - width, ff[0] + width + 1): #starts line under base thru bottom peak
                if c > mx or c < 0 or r > mx or r < 0: #checks if its too big or too small for area of concern
                    continue
                grid[(r, c)] = None
            width -= 1
        progress += 1
    #print(sorted([g for g in grid if 0 <= g[0] <= mx and 0 <= g[1] <= mx]))
    print("Starting To Look For Missing")
    #return missing(mx)
    #return "*****WIP*****"


def manhat(a, b):
    aa = abs(a[0] - b[0])
    bb = abs(a[1] - b[1])
    return aa + bb

def missing(mx):
    for row in range(mx):
        for column in range(mx):
            if (row, column) not in grid:
                return (column * 4000000) + row
    

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    mx = 4000000
    print("Result:", numFind(mx))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")