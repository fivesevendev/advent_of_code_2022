#AOC-2022-1-2


import timeit
import time


def numFind(n):
    cals = []
    with open("1.txt") as f:
        f = f.read()
    f = [list(map(int, x.split("\n"))) for x in f.split("\n\n")]
    for fsum in f:
        cals.append(sum(fsum))
    return sum(sorted(cals)[-3:])


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")