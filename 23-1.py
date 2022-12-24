#AOC-2022-23-1


import timeit
import time
from collections import deque
from copy import deepcopy


dir_order = deque(["north", "south", "west", "east"])


def numFind(n):
    global elves
    elves = deque()
    steps = 0
    with open("23.txt") as f:
        f = f.read()
    f = f.splitlines()
    for row in range(len(f)):
        for col in range(len(f[row])):
            if  f[row][col] == "#":
                elves.append((row, col))

    while steps < n:
        moved_elves = {}
        new_elves = deque()
        for m_f in elves:
            if needToMove(m_f):
                for direction in dir_order:
                    if direction == "north":
                        m_t = (m_f[0] - 1, m_f[1])
                        if (m_f[0] - 1, m_f[1] - 1) not in elves and (m_f[0] - 1, m_f[1]) not in elves and (m_f[0] - 1, m_f[1] + 1) not in elves:
                            moved_elves[m_f] = m_t
                            break
                    elif direction == "south":
                        m_t = (m_f[0] + 1, m_f[1])
                        if (m_f[0] + 1, m_f[1] - 1) not in elves and (m_f[0] + 1, m_f[1]) not in elves and (m_f[0] + 1, m_f[1] + 1) not in elves:
                            moved_elves[m_f] = m_t
                            break
                    elif direction == "west":
                        m_t = (m_f[0], m_f[1] - 1)
                        if (m_f[0] - 1, m_f[1] - 1) not in elves and (m_f[0], m_f[1] - 1) not in elves and (m_f[0] + 1, m_f[1] - 1) not in elves:
                            moved_elves[m_f] = m_t
                            break
                    elif direction == "east":
                        m_t = (m_f[0], m_f[1] + 1)
                        if (m_f[0] - 1, m_f[1] + 1) not in elves and (m_f[0], m_f[1] + 1) not in elves and (m_f[0] + 1, m_f[1] + 1) not in elves:
                            moved_elves[m_f] = m_t
                            break
                else:
                    #no movement at all possible:
                    #print("can't move", m_f)
                    moved_elves[m_f] = m_f
            else:
                #print("no move:", m_f)
                new_elves.append(m_f) #adds unmoved tuple to new_elves list

        for x, y in moved_elves.items():
            if list(moved_elves.values()).count(y) > 1: #checks for move conflicts/duplicates
                new_elves.append(x) #re-adds moved from pos to new elves
            else:
                new_elves.append(y) #adds moved to pos to new elves

        del(elves)
        elves = deque(deepcopy(list(new_elves)))
        del(new_elves)
        del(moved_elves)
        dir_order.append(dir_order.popleft())
        steps += 1
    
    row_list = [rl[0] for rl in elves] #creates list of rows occupied
    eHeight = max(row_list) - min(row_list) + 1 #gets the bounded height of rows that elves occupy, +1 accounts for row 0
    col_list = [cl[1] for cl in elves] #creates list of cols occupied
    eWidth = max(col_list) - min(col_list) + 1 #gets the bounded width of cols that elves occupy, +1 accounts for col 0
    max_spots = eHeight * eWidth #maximum number of spots available in bounds
    open_spots = max_spots - len(elves) # determines unoccupied spots in bounds
    return open_spots

def needToMove(m):
    if (m[0] - 1, m[1] - 1) in elves or (m[0] - 1, m[1]) in elves or (m[0] - 1, m[1] + 1) in elves: #checks NW, N, NE
        return True
    if (m[0], m[1] - 1) in elves or (m[0], m[1] + 1) in elves: #checks W, E
        return True
    if (m[0] + 1, m[1] - 1) in elves or (m[0] + 1, m[1]) in elves or (m[0] + 1, m[1] + 1) in elves: #checks SW, S, SE
        return True
    return False


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 10
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")