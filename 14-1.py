#AOC-2022-14-1


import timeit
import time


def numFind():
    maze = {}
    
    with open("14.txt") as f:
        f = f.read()
    f = [s.split(" -> ") for s in f.split("\n")]
    for t in range(len(f)):
        for tt in range(len(f[t])):
            f[t][tt] = tuple(map(int, f[t][tt].split(","))) #creates lists of tuples to build the maze lines from
    
    for ff in f:
        print(ff)
    
    for line in range(len(f) - 1):
        print(f[line][0][0])




if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")