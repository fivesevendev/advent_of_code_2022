#AOC-2022-2-2


import timeit
import time


key = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
throw = ['C', 'A', 'B']

def numFind(n):
    score = 0
    with open("2.txt") as f:
        f = f.read()
    f = [tuple(x.split(" ")) for x in f.split("\n")]
    for i, j in f:
        if j == "X":
            score += key[throw[(throw.index(i) + 2) % 3]]
        elif j == "Z":
            score += key[throw[(throw.index(i) + 1) % 3]] + 6
        else:
            score += key[i] + 3
    return score


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")