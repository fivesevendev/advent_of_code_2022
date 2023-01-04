#AOC-2022-12-2


import timeit
import time


def numFind():
    distance = 0
    COST, HEIGHT, PARENT = 0, 1, 2 #index marking constants
    ROW, COL = 0, 1 #index marking constants
    BIGNUM = 1234567891011121314 #arbitrary large number for default cost
    checked = {}
    unchecked = {}

    with open("12.txt") as f:
        f = f.read()
    f = [list(s) for s in f.split("\n")]
    
    for fr in range(len(f)):
        if "S" in f[fr]:
            startPos = (fr, f[fr].index("S")) #determines and sets the start positions
        if "E" in f[fr]:
            endPos = (fr, f[fr].index("E")) #determines and sets ending position
        for fc in range(len(f[fr])):
            unchecked[fr, fc] = [BIGNUM, ord(f[fr][fc]), None]
    unchecked[startPos][COST] = 0 #sets start pos cost to 0
    unchecked[startPos][HEIGHT] = 96 #sets starting height 1 less than ord("a")
    unchecked[endPos][HEIGHT] = 123 #sets ending height 1 more than ord("z")
    
    for everyA in [aaa for aaa in unchecked if unchecked[aaa][HEIGHT] == 97]: #adds every "a" starting pos to unchecked with 0 cost
        unchecked[everyA][COST] = 0

    doneChecking = False
    while not doneChecking:
        if len(unchecked) == 0: #ends while loop if unchecked positions are depleted
            doneChecking = True
        else:
            cPos = min(unchecked, key=unchecked.get) #selects the next position with the lowest cost
            distance += 1
            potentials = [(cPos[ROW] - 1, cPos[COL]), (cPos[ROW] + 1, cPos[COL]), (cPos[ROW], cPos[COL] - 1), (cPos[ROW], cPos[COL] + 1)] #creates list of 4 potential moves
            for pot in potentials: #for all possible moves
                if pot not in checked: #ensure we haven't checked them already
                    if pot in unchecked: #ensure they exist within the grid provided
                        if unchecked[pot][HEIGHT] <= unchecked[cPos][HEIGHT] + 1: #ensures move is at most 1 elev higher than current elev
                            #cost = manhat(pot, endPos) #cost based only on manhat value
                            #cost = manhat(pot, endPos) + distance #cost based on manhat value and distance already traveled
                            cost = distance #cost based only on distance alread traveled
                            if cost < unchecked[pot][COST]: #if cost(manhat distance) is less than BIGNUM
                                unchecked[pot][COST] = cost #update COST of the pos
                                unchecked[pot][PARENT] = cPos #update PARENT of the pos
                                if pot == endPos:
                                    break
            checked[cPos] = unchecked[cPos] #adds cPos to the checked pos dict
            del unchecked[cPos] #removes cPos from unchecked

    #for chkd in checked.items():
    #    print(chkd)
    
    steps = 0
    backTrack = endPos #starts at the end position
    while backTrack != startPos:
        try:
            backTrack = checked[backTrack][PARENT] #traces steps backwards to start pos
            steps += 1
        except KeyError:
            steps -= 1 #subtracts one erroneously counted step
            break
        
    return steps #returns min steps to reach start from end


def manhat(a, b):
    aa = abs(a[0] - b[0])
    bb = abs(a[1] - b[1])
    return aa + bb


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")