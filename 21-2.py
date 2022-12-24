#AOC-2022-21-2


import timeit
import time
from collections import deque


def numFind():
    humn = 3272260914300 #a lot of manual testing went into finding this starting point
    while True:
        with open("21-2.txt") as f:
            f = f.read()
        f = [[ss for ss in s.split(": ")] for s in f.splitlines()]
        we_yell = {}
        we_do_math = deque()
        known = {}
    
        for _ in range(len(f)):
            div_sort = f.pop()
            if div_sort[1].isnumeric():
                we_yell[div_sort[0]] = int(div_sort[1]) #creates entries for yeller with single values
            else:
                we_do_math.append([div_sort[0], div_sort[1]]) #creates entries for yellers who do math
        we_yell['humn'] = humn
        for yeller in we_yell.items():
            known[yeller[0]] = int(yeller[1]) #adds single value yeller values to known registry
        
        while we_do_math != deque(): #cycles until all values known
            mather = we_do_math.popleft()
            a, b, c = mather[1].split(" ") #splits out the expression from mather
            if a in known and c in known:
                aa = known[a]
                cc = known[c]
                known[mather[0]] = eval(str(aa) + b + str(cc)) #if all values known do expression and add to known
            else:
                we_do_math.append(mather) #if not all values known, add back to end of the list to do again later
        if known['tcmj'] == known['qggp']:
            return known['humn']
        humn += 1


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")