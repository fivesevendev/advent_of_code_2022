#AOC-2022-10-2


import timeit
import time


def numFind(n):
    crt = list(".") * 240
    cycle = 0
    x = 0
    with open("10.txt") as f:
        f = f.read()
    f = f.split("\n")
    for op in f:
        if op[:4] == "noop":
            if spriteCRT(cycle, x):
                crt[cycle] = "#"
            cycle += 1
        else:
            cmd, v = op.split(" ")
            if spriteCRT(cycle, x):
                crt[cycle] = "#"
            cycle += 1
            if spriteCRT(cycle, x):
                crt[cycle] = "#"
            cycle += 1
            x += int(v)
    for pixels in [0, 40, 80, 120, 160, 200]:
        print(str(crt[pixels: pixels + 40]).replace("'", "").replace(",", "").replace(".", " "))

def spriteCRT(cycle, x):
    return (cycle % 40) - 1 == x - 1 or (cycle % 40) - 1 == x or (cycle % 40) - 1 == x + 1


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    numFind(n)
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")