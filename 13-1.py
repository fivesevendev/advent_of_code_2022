#AOC-2022-13-1


import timeit
import time
from itertools import zip_longest


def numFind():
    correctOrderIndices = []
    pairNum = 0
    with open("13.txt") as f:
        f = f.read()
    f = [[fs for fs in s.split("\n")] for s in f.split("\n\n")]
    for fl, fr in f:
        fl, fr = eval(fl), eval(fr)
        pairNum += 1
        if versus(fl, fr):
            correctOrderIndices.append(pairNum) #adds pairNum to list of correct pairs
    return sum(correctOrderIndices) #returns sum of correct pairNums

def versus(fl, fr):
    for l, r in zip_longest(fl, fr):
        output = None
        if type(l) == int and type(r) == int: #checks int vs int and returns if definitive but not the same
            if l < r:
                return True
            elif l > r:
                return False
        elif type(l) == list and type(r) == list: #checks if list vs list and recurs
            output = versus(l, r)
        elif type(l) == list and type(r) == int: #checks if list vs single int and recurs as list vs list
            output = versus(l, [r])
        elif type(l) == int and type(r) == list: #checks if single int and list and recurs as list vs list
            output = versus([l], r)
        elif l == None: #checks if vals have run out on the left
            return True
        elif r == None: #checks if vals have run out on the right
            return False
        if output != None: #checks for output of any recursions that aren't None
            return output


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")