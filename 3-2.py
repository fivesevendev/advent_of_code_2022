#AOC-2022-3-2


import timeit
import time


def numFind(n):
    output = 0
    with open("3.txt") as f:
        f = f.read()
    f = [s for s in f.split("\n")]
    for i in range(0, len(f), 3):
        a, b, c = map(set, f[i:i + 3])
        x = list(a.intersection(b).intersection(c))[0]
        output += priority(x)
    return output        

def priority(n):
    if n.islower():
        return (ord(n) - 96)
    return ord(n) - 38


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")