#AOC-2022-2-1


import timeit
import time


key = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
ndkey = {('A','X'):3, ('A', 'Y'):6, ('A', 'Z'):0, ('B','X'):0, ('B','Y'):3, ('B', 'Z'):6, ('C', 'X'):6, ('C', 'Y'):0, ('C', 'Z'):3}


def numFind(n):
    score = 0
    with open("2.txt") as f:
        f = f.read()
    f = [tuple(x.split(" ")) for x in f.split("\n")]
    for i, j in f:
        score += key[j] + ndkey[(i, j)]
    return score


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")