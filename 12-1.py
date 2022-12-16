#AOC-2022-12-1


import timeit
import time
from random import shuffle


def numFind():
    posValues = {}
    blackList = {}
    nextMove = 97
    step = 0
    
    with open("12.txt") as f:
        f = f.read()
    f = [list(s) for s in f.split("\n")]
    for fr in range(len(f)):
        if "S" in f[fr]:
            cPos, startPos = [fr, f[fr].index("S")], [fr, f[fr].index("S")] #determines and sets current and start positions
        if "{" in f[fr]:
            ePos = [fr, f[fr].index("{")] #determines and sets ending/target position
        for fc in range(len(f[fr])):
            posValues[fr, fc] = f[fr][fc]
    
    #print("Start: ", startPos)
    pathTaken = {tuple(cPos): step}
    while True:
        checkList = [[cPos[0] - 1, cPos[1]], [cPos[0] + 1, cPos[1]], [cPos[0], cPos[1] - 1], [cPos[0], cPos[1] + 1]] #checks up, down, left, right
        shuffle(checkList)
        for checkCoord in checkList:
            if tuple(checkCoord) in posValues: #checks that position is in the grid values
                #print("Pos {} is {}:{} looking for {}:{}".format(checkCoord, ord(posValues[tuple(checkCoord)]), posValues[tuple(checkCoord)], nextMove, chr(nextMove)))
                if ord(posValues[tuple(checkCoord)]) <= nextMove: #checks if value is less than or equal to the move we are looking for
                    if tuple(checkCoord) not in pathTaken: #check we haven't been here before
                        if tuple(checkCoord) not in blackList: #check we haven't been stuck here before                        
                            step += 1
                            pathTaken[tuple(checkCoord)] = step #add new step to the pathtaken
                            cPos = list(checkCoord) #makes new step current step
                            nextMove = ord(posValues[tuple(checkCoord)]) + 1
                            #print("Step", step)
                            #print("Current Position", cPos)
                            #print("BROKEN")
                            #time.sleep(1)
                            break
        else:                            
            #print("Blacklisted")
            blackList[tuple(cPos)] = 0
            #print("Starting Over")
            #print("Path Taken", pathTaken)
            #print("Black List", blackList)
            #print("")
            nextMove = 97
            step = 0
            cPos = list(startPos)
            pathTaken = {tuple(cPos): step}
            #time.sleep(1)

        if cPos == ePos:
            #print(pathTaken)
            #print([posValues[s] for s in pathTaken])
            return len(pathTaken) - 1

# 480 least so far

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    shortest = 1000
    for _ in range(20):
        test = numFind()
        if test < shortest:
            shortest = test
    print("Result:", shortest)
    print("*****WIP*****")
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")