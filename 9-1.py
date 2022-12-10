#AOC-2022-9-1


import timeit
import time


def numFind(n):
    tTrail = {}
    hPos = [1, 1]
    tPos = [1, 1]
    with open("9.txt") as f:
        f = f.read()
    f = [s.split(" ") for s in f.split("\n")]
    for move in f:
        if move[0] == "U":
            for _ in range(int(move[1])):
                oldH = list(hPos)
                hPos[0] += 1
                tPos = tailFollow(hPos, tPos, oldH)
                tTrail[tuple(tPos)] = True
        elif move[0] == "D":
            for _ in range(int(move[1])):
                oldH = list(hPos)
                hPos[0] -= 1
                tPos = tailFollow(hPos, tPos, oldH)
                tTrail[tuple(tPos)] = True
        elif move[0] == "L":
            for _ in range(int(move[1])):
                oldH = list(hPos)
                hPos[1] -= 1
                tPos = tailFollow(hPos, tPos, oldH)
                tTrail[tuple(tPos)] = True
        elif move[0] == "R":
            for _ in range(int(move[1])):
                oldH = list(hPos)
                hPos[1] += 1
                tPos = tailFollow(hPos, tPos, oldH)
                tTrail[tuple(tPos)] = True
    return list(tTrail.values()).count(True)

def tailFollow(hPos, tPos, oldH):
    if  abs(hPos[0] - tPos[0]) > 1 or abs(hPos[1] - tPos[1]) > 1:
        return oldH
    return tPos


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")