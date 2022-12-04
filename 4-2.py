#AOC-2022-4-2


import timeit
import time


def numFind(n):
    count = 0
    with open("4.txt") as f:
        f = f.read()
    f = f.replace("-", ",")
    f = [s.split(",") for s in f.split("\n")]
    for a,b,x,y in f:
        s1 = set(range(int(a), int(b) + 1))
        s2 = set(range(int(x), int(y) + 1))
        if s1.intersection(s2):
            count += 1
    return count


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")