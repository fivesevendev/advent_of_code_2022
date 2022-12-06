#AOC-2022-5-1


import timeit
import time


data = [
        ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
        ['G', 'W', 'M'],
        ['J', 'N', 'H', 'G'],
        ['J', 'R', 'C', 'N', 'W'],
        ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
        ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
        ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
        ['S', 'J', 'N', 'M', 'G', 'C'],
        ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']
]


def numFind(n):
    output = []
    with open("5.txt") as f:
        f = f.read()
    f = f.replace("move ", "").replace("from ", "").replace("to ", "")
    f = [list(map(int, s.split(" "))) for s in f.split("\n")]
    for moveq, movef, movet in f:
        mq = 0
        while mq < moveq:
            n[movet - 1].append(n[movef - 1].pop())
            mq += 1
    for x in n:
        if x:
            output.append(x[-1])
    return "".join(output)


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = data
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")