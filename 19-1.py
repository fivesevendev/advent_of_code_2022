#AOC-2022-19-1


import timeit
import time
from copy import deepcopy

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
        bluePrints[a] = deepcopy({'geode': [f, 0, g], 'obsidian': [d, e, 0], 'clay': [c, 0, 0], 'ore': [b, 0, 0]})
    
    q = deepcopy(bluePrints[1]) #this will eventually be a for loop that includes the while loop for all blueprints in bluePrints
    max_mat = {'ore': 0, 'clay':0, 'obsidian': 0, 'geode':1000}
    
    for mxmat in q.values(): #creates upper limit targets for robot building based on resources
        max_mat['ore'] = deepcopy(max(mxmat[0], max_mat['ore']))
        max_mat['clay'] = deepcopy(max(mxmat[1], max_mat['clay']))
        max_mat['obsidian'] = deepcopy(max(mxmat[2], max_mat['obsidian']))
    
    max_ore = deepcopy(max_mat['ore'])
    max_clay = deepcopy(max_mat['clay'])
    max_obsidian = deepcopy(max_mat['obsidian'])
    
    for test_ore in range(0, max_ore + 1):
        max_mat['ore'] = deepcopy(test_ore)
        max_mat['clay'] = deepcopy(max_clay)
        max_mat['obsidian'] = deepcopy(max_obsidian)

        for test_clay in range(0, max_clay + 1):
            max_mat['clay'] = deepcopy(test_clay)
            max_mat['obsidian'] = deepcopy(max_obsidian)

            for test_obsidian in range(0, max_obsidian + 1):
                max_mat['obsidian'] = deepcopy(test_obsidian)
                
                mats = [0, 0, 0, 0] #[ore, clay, obsidian, geode]
                collecting = ['ore']
                minutes = 1
                while minutes <= time_limit:
                    new_collector = ""
                    for robots in q.items():
                        if collecting.count(robots[0]) < max_mat[robots[0]]: #only purchase robot if make max not met
                            #if mats[0] >= robots[1][0] and mats[1] >= robots[1][1] and mats[2] >= robots[1][2]: #compares robot cost to mats, ignores geodes ##TOO SIMPLE
                            if mats[0] >= robots[1][0] and mats[1] >= robots[1][1] and mats[2] >= robots[1][2]:                                
                                new_collector = deepcopy(robots[0])
                                mats = deepcopy([mats[0] - robots[1][0], mats[1] - robots[1][1], mats[2] - robots[1][2], mats[3]])
                                break #breaks the for loop due to single purchase in cycle
                    #print("== Minute", minutes, "==")
                    for bot in range(len(bots)):
                        mats[bot] += collecting.count(bots[bot]) #adds mats from each collecting robot to mats

                    if new_collector != "":
                        collecting.append(new_collector) #adds freshly built robot to collecting

                    minutes += 1
                if mats[3] > 0: max_geodes.append(mats[3])
    print("Run Outcomes:", max_geodes)
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