#AOC-2022-25-1


import timeit
import time
from copy import deepcopy


sKey = {"2": 2, "1":1, "0":0, "-":-1, "=":-2}
fives = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 30517578125, 152587890625, 762939453125, 3814697265625, 19073486328125, 95367431640625, 476837158203125, 2384185791015625, 11920928955078125, 59604644775390625]


def numFind():
    with open("25.txt") as f:
        f = f.read()
    f = [list(s) for s in f.splitlines()]
    total = 0
    for ef in f:
        total += unSnafu(ef)
    return snafu(total)

def snafu(sN):
    position = 0
    current_num = 0
    target = int(sN)
    build_point = 0
    for five in range(len(fives)):
        build_point += fives[five] * 2
        if build_point >= sN:
            working_range = deepcopy(fives[:five + 1][::-1])
            output = list("0" * (five + 1))
            break
    for slot in working_range:
        closest = 10**1000
        pTwo = (current_num + (slot * 2)) - target
        pOne = (current_num + (slot * 1)) - target
        zZero = (current_num + 0) - target
        nOne = (current_num + (slot * -1)) - target
        nTwo = (current_num + (slot * -2)) - target
        if abs(pTwo) < closest: closest = pTwo
        if abs(pOne) < closest: closest = pOne
        if abs(zZero) < closest: closest = zZero
        if abs(nOne) < closest: closest = nOne
        if abs(nTwo) < closest: closest = nTwo
        if pTwo == closest:
            output[position] = "2"
        elif pOne == closest:
            output[position] = "1"
        elif zZero == closest:
            output[position] = "0"
        elif nOne == closest:
            output[position] = "-"
        elif nTwo == closest:
            output[position] = "="
        position += 1
        current_num = unSnafu(output)
    return "".join(output)

def unSnafu(u_sN):
    output = 0
    for u, v in list(enumerate(u_sN[::-1])):
        output += ((5 ** u) * sKey[v]) #turns snafu number into decimal number
    return output


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")