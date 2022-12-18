#AOC-2022-17-1


import timeit
import time
from copy import deepcopy


tetris = {(0,1):"-",(0,2):"-",(0,3):"-",(0,4):"-",(0,5):"-",(0,6):"-",(0,7):"-",}
shape_order = ['horz', 'plus', 'corner', 'vert', 'square']


def numFind(n):
    rocks = 0
    maxHeight = 0
    sOrder, sLen = 0, len(shape_order)
    with open("17.txt") as f:
        f = f.read()
    f = list(f)
    jOrder, jLen = 0, len(f)
    while rocks < n:
        piece = shape_order[sOrder]
        sPos = shape_builder(piece, maxHeight)
        dropping = True
        while dropping: #place while loop here eventually
            sPos = shape_push(sPos, f[jOrder]) #pushes the shape one position
            sPos, dropping = shape_drop(sPos) #drops the shape one position
            jOrder = (jOrder + 1) % jLen #selects the next direction to push
        rocks += 1
        sOrder = (sOrder + 1) % sLen #selects the next shape to drop
        for coord in sPos:
            tetris[tuple(coord)] = "#" #adds all rested segments to tetris
        maxHeight = max(tetris)[0]
    return max(tetris)[0] #gives height of highest piece in tetris


def shape_builder(shape, bottom):
    bottom += 4
    if shape == "horz":
        shape_pos = [[bottom, 3], [bottom, 4], [bottom, 5], [bottom, 6]]
    elif shape == "plus":
        shape_pos = [[bottom, 4], [bottom + 1, 3], [bottom + 1, 4], [bottom + 1, 5], [bottom + 2, 4]]
    elif shape == "corner":
        shape_pos = [[bottom, 3], [bottom, 4], [bottom, 5], [bottom + 1, 5], [bottom + 2, 5]]
    elif shape == "vert":
        shape_pos = [[bottom, 3], [bottom + 1, 3], [bottom + 2, 3], [bottom + 3, 3]]
    elif shape == "square":
        shape_pos = [[bottom, 3], [bottom, 4], [bottom + 1, 3], [bottom + 1, 4]]
    return shape_pos

def shape_drop(drop_pos):
    old_drop = deepcopy(drop_pos)
    for segDrop in range(len(drop_pos)):
        drop_pos[segDrop][0] = drop_pos[segDrop][0] - 1 #drops all row positions by 1
    if rested(drop_pos) == True:
        return (old_drop, False)
    return (drop_pos, True)

def shape_push(push_pos, direction):
    old_push = deepcopy(push_pos)
    if direction == ">":
        direction = 1
    elif direction == "<":
        direction = -1
    for segPush in range(len(push_pos)):
        push_pos[segPush][1] = push_pos[segPush][1] + direction #pushes all column positions by 1
    if collision(push_pos) == True:
        return old_push
    return push_pos

def rested(shape_pos):
    for segRested in shape_pos:
        if tuple(segRested) in tetris:
            return True
    return False

def collision(shape_pos):
    for segCollision in shape_pos:
        if segCollision[1] > 7 or segCollision[1] < 1 or tuple(segCollision) in tetris:
            return True
    return False


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 2022
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")