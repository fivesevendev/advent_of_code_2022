#AOC-2022-19-1


import timeit
import time
import sys

def numFind(time_limit):
    bluePrints = {} #this dict gets built by the ridiculous parser
    max_geodes = []
    bots = ['ore', 'clay', 'obsidian', 'geode']
    bpData = []
    with open("19.txt") as f:
        f = f.read()
    f = [[ss for ss in s.split(". ")] for s in f.split("\n")]
    for bp in range(len(f)):
        new_cost = []
        for cost in range(len(f[bp])):
            f[bp][cost] = f[bp][cost].replace(":", " :")
            for x in f[bp][cost].split(" "):
                if x.isnumeric():
                    new_cost.append(x)
        bpData.append(list(map(int, new_cost)))
    for a,b,c,d,e,f,g in bpData: #builds the bluePrints dict with list of robots and mat costs as [ore, clay, obsidian]
        #bluePrints[a] = {'ore': [b, 0, 0], 'clay': [c, 0, 0], 'obsidian': [d, e, 0], 'geode': [f, 0, g]}
        bluePrints[a] = {'geode': [f, 0, g], 'obsidian': [d, e, 0], 'clay': [c, 0, 0], 'ore': [b, 0, 0]}
    
    q = bluePrints[1] #this will eventually be a for loop that includes the while loop for all blueprints in bluePrints
    #print("q:", q)
    max_mat = {'ore': 0, 'clay':0, 'obsidian': 0, 'geode':1000}
    for mxmat in q.values(): #creates upper limit targets for robot building based on resources
        #print(mxmat)
        max_mat['ore'] = max(mxmat[0], max_mat['ore'])
        max_mat['clay'] = max(mxmat[1], max_mat['clay'])
        max_mat['obsidian'] = max(mxmat[2], max_mat['obsidian'])
    #print("max ore:", max_mat['ore'])
    #print("max clay:", max_mat['clay'])
    #print("max obsidian:", max_mat['obsidian'])
    max_ore = max_mat['ore']
    max_clay = max_mat['clay']
    max_obsidian = max_mat['obsidian']
    
    for test_ore in range(0, max_ore + 1):
        max_mat['ore'] = test_ore
        for test_clay in range(0, max_clay + 1):
            max_mat['clay'] = test_clay
            for test_obsidian in range(0, max_obsidian + 1):
                max_mat['obsidian'] = test_obsidian
                #print("testing maxes:", [test_ore, test_clay, test_obsidian])
                mats = [0, 0, 0, 0] #[ore, clay, obsidian, geode]
                collecting = ['ore']
                minutes = 1
                while minutes <= time_limit:
                    new_collector = ""
                    for robots in q.items():
                        if mats[0] >= robots[1][0] and mats[1] >= robots[1][1] and mats[2] >= robots[1][2]: #compares robot cost to mats, ignores geodes
                            if collecting.count(robots[0]) - 1 == max_mat[robots[0]]: #skips purchasing robot model if max is already reached, looks to other models
                                #print(robots[0], "max reached********************************************************")
                                continue                
                            new_collector = robots[0]
                            mats = [mats[0] - robots[1][0], mats[1] - robots[1][1], mats[2] - robots[1][2], mats[3]] 
                            break #breaks the for loop due to single purchase in cycle
                    #print("== Minute", minutes, "==")
                    if new_collector != "":
                        pass
                        #print("Building:", new_collector)
                    for bot in range(len(bots)):
                        mats[bot] += collecting.count(bots[bot]) #adds mats from each collecting robot to mats
                    #print("After Collecting Working Cycle:", collecting)
                    #print("After Mats Working Cycle:", mats)
                    if new_collector != "":
                        collecting.append(new_collector) #adds freshly built robot to collecting
                        #print("Ready:", new_collector)
                    #print()
                    #time.sleep(1)
                    minutes += 1
                #print("Geodes: {}".format(mats[3]))
                max_geodes.append(mats[3])
    
    return "Max Geodes: {}".format(max(max_geodes))

# determine steps to get first geode cracker(work backwards from 1 geode robot), create a path and ensure first steps of the purchaser follow that path
#
#
#
#

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 24
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")