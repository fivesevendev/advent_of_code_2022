#AOC-2022-10-1


import timeit
import time


def numFind(n):
    output = 0
    sigs = [20, 60, 100, 140, 180, 220]
    cycle = 1
    x = 1
    cycReg = {cycle: x}
    with open("10.txt") as f:
        f = f.read()
    f = f.split("\n")
    for op in f:
        if op[:4] == "noop":
            cycle += 1
            cycReg[cycle] = x
        else:
            cmd, v = op.split(" ")
            cycle += 1
            cycReg[cycle] = x
            cycle += 1
            x += int(v)
            cycReg[cycle] = x
    for s in sigs:
        output += cycReg[s] * s
    return output


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")