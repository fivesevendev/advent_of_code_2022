#AOC-2022-13-2


import timeit
import time


def numFind():
    flatF = []
    pairNum = 0
    with open("13.txt") as f:
        f = f.read()
    f = [[fs for fs in s.split("\n")] for s in f.split("\n\n")]
    for fl, fr in f:
        flatF.extend([flatten(fl), flatten(fr)])
    flatF.extend([[2], [6]])
    firstPacket =  sorted(flatF).index([2]) + 1
    secondPacket = sorted(flatF).index([6]) + 1
    return firstPacket * secondPacket

def flatten(n):
    mList = str(n).replace("[]", "-1").replace(" ", "")
    mList = mList.replace("[", "").replace("]", "")
    return list(map(int, mList.split(",")))


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")