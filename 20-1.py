#AOC-2022-20-1


import timeit
import time
from copy import deepcopy


def numFind():
    with open("20.txt") as f:
        f = f.read()
    f = list(map(int, f.splitlines()))
    zeroTuple = f.index(0) #gets original list location for 0 value
    f = list(enumerate(f)) #normalizes not unique values
    zeroTuple = (zeroTuple, 0) #creates tuple for original zero value so we know what to look for later
    act_len = len(f) #used at the end for locating the coords with the full list
    mod_len = len(f) - 1 #accounts for the missing value during moving
    original = deepcopy(f) #duplicates the list for paired walking and the original doesn't change order
    for value in original:
        old_loc = f.index(value) #gets index location of value
        f.pop(old_loc) #removes value based on index location
        target = old_loc + value[1]
        f.insert(target % mod_len, value)
    zero = f.index(zeroTuple) #simpler zero variable to look for and return result
    return f[(zero + 1000) % act_len][1] + f[(zero + 2000) % act_len][1] + f[(zero + 3000) % act_len][1]


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")