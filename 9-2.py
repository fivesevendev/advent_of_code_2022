#AOC-2022-9-2


import timeit
import time


def numFind(n):
    tTrail = {}
    tailsPos = {0:[1, 1], 1:[1, 1], 2:[1, 1], 3:[1, 1], 4:[1, 1], 5:[1, 1], 6:[1, 1], 7:[1, 1], 8:[1, 1], 9:[1, 1]}
    with open("9.txt") as f:
        f = f.read()
    f = [s.split(" ") for s in f.split("\n")]
    for move in f:
        if move[0] == "U":
            for _ in range(int(move[1])):
                tailsPos[0][0] += 1
                for knots in range(1, len(tailsPos)):
                    tailsPos[knots] = tailFollow(tailsPos[knots - 1], tailsPos[knots])
                tTrail[tuple(tailsPos[9])] = True
        elif move[0] == "D":
            for _ in range(int(move[1])):
                tailsPos[0][0] -= 1
                for knots in range(1, len(tailsPos)):
                    tailsPos[knots] = tailFollow(tailsPos[knots - 1], tailsPos[knots])
                tTrail[tuple(tailsPos[9])] = True
        elif move[0] == "L":
            for _ in range(int(move[1])):
                tailsPos[0][1] -= 1
                for knots in range(1, len(tailsPos)):
                    tailsPos[knots] = tailFollow(tailsPos[knots - 1], tailsPos[knots])
                tTrail[tuple(tailsPos[9])] = True
        elif move[0] == "R":
            for _ in range(int(move[1])):
                tailsPos[0][1] += 1
                for knots in range(1, len(tailsPos)):
                    tailsPos[knots] = tailFollow(tailsPos[knots - 1], tailsPos[knots])
                tTrail[tuple(tailsPos[9])] = True
    return list(tTrail.values()).count(True)

def tailFollow(hPos, tPos):
    if  abs(hPos[0] - tPos[0]) > 1 or abs(hPos[1] - tPos[1]) > 1:
        r = round((hPos[0] + hPos[0] + tPos[0]) / 3)
        c = round((hPos[1] + hPos[1] + tPos[1]) / 3)
        return [r, c]
    return tPos


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")