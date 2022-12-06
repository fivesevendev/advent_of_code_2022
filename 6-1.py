#AOC-2022-6-1


import timeit
import time


def numFind(n):
    with open("6.txt") as f:
        f = f.read()
    for r in range(len(f) - 3):
        if len(set(f[r:r + 4])) == 4:
            return r + 4
        

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")