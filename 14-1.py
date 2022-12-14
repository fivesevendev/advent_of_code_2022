#AOC-2022-14-1


import timeit
import time


def numFind():
    maze = {}
    voided = False
    sandPos = [0, 500]
    with open("14.txt") as f:
        f = f.read()
    f = [s.split(" -> ") for s in f.split("\n")]
    for t in range(len(f)):
        for tt in range(len(f[t])):
            f[t][tt] = tuple(map(int, f[t][tt].split(","))) #creates lists of tuples to build the maze lines from
    for line in f: #gets single line from f
        for entry in range(len(line) - 1): #walks entries in line as a slice number for forward ranging
            for r in range(min(line[entry][1], line[entry + 1][1]), max(line[entry][1], line[entry + 1][1]) + 1): #creates for loop for row from min to max
                for c in range(min(line[entry][0], line[entry + 1][0]), max(line[entry][0], line[entry + 1][0]) + 1): #creates for loop for column from min to max
                    maze[(r, c)] = "#" #creates maze walls in maze dict    
    while not voided:
        rested = False
        sandPos = [0, 500]
        while not rested:
            if (sandPos[0] + 1, sandPos[1]) in maze: #checks if we hit something going down
                if (sandPos[0] + 1, sandPos[1] - 1) not in maze: #can we go diag left-down
                    sandPos[1] -= 1
                elif (sandPos[0] + 1, sandPos[1] + 1) not in maze: #we can't go left, can we go diag right-down
                    sandPos[1] += 1
                else: #we can't go diag left-down or right-down
                    maze[tuple(sandPos)] = "o"
                    rested = True
            sandPos[0] += 1
            if sandPos[0] > max(maze)[0]: #checks to see if sand has fallen past lowest point of the maze
                voided = True
                rested = True
    return list(maze.values()).count("o")


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")