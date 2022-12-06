#AOC-2022-6-2


import timeit
import time


def numFind(n):
    with open("6.txt") as f:
        f = f.read()
    for r in range(len(f) - 13):
        if len(set(f[r:r + 14])) == 14:
            return r + 14
        

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")