#AOC-2022-19-1


import timeit
import time


def numFind(time_limit):
    bluePrints = {} #this dict gets built by the ridiculous parser
    mats = [0, 0, 0, 0] #[ore, clay, obsidian, geode]
    collecting = ['ore']
    bots = ['ore', 'clay', 'obsidian', 'geode']
    minutes = 1
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
    #print("Collecting Start:", collecting)
    #print("Mats Start: ", mats)
    while minutes <= time_limit:
        new_collector = ""
        for robots in q.items():
            if mats[0] >= robots[1][0] and mats[1] >= robots[1][1] and mats[2] >= robots[1][2]: #compares robot cost to mats, ignores geodes
                new_collector = robots[0]
                #collecting.append(robots[0]) #if affordable adds robot to collecting list
                mats = [mats[0] - robots[1][0], mats[1] - robots[1][1], mats[2] - robots[1][2], mats[3]] 
                break #breaks the for loop due to single purchase in cycle
                #subtracts the cost of the robot added to collecting
        print("== Minute", minutes, "==")
        if new_collector != "":
            print("Building:", new_collector)
        #print("After Collecting Purchase Cycle:", collecting)
        #print("After Mats Purchase Cycle:", mats)
        #print()
        for bot in range(len(bots)):
            mats[bot] += collecting.count(bots[bot]) #adds mats from each collecting robot to mats
        #print("After Working Cycle:", minutes)
        print("After Collecting Working Cycle:", collecting)
        print("After Mats Working Cycle:", mats)
        
        if new_collector != "":
            collecting.append(new_collector) #adds freshly built robot to collecting
            print("Ready:", new_collector)
        print()
        #time.sleep(1)
        minutes += 1
    return "Geodes: {}".format(mats[3])


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 24
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")