#AOC-2022-7-1


import timeit
import time


def numFind(n):
    tree = {}
    pwd = ""
    o = 0
    with open("7.txt") as f:
        f = f.read()
    f = [s.split(" ") for s in f.split("\n")]
    print(f)
    #for o in f:
    while o < len(f):
        #print(f[o])
        #Start command checking
        if f[o][0] == "$":
            if f[o][1] == "cd":
                if f[o][2] == "..":
                    pwd = pwd[:pwd[:-1].rfind("/") + 1]
                    if pwd == "":
                        pwd = "/"
                else:
                    pwd = pwd + f[o][2] + "/"
                if pwd[:2] == "//":
                    pwd = pwd[1:]
                if pwd not in tree:
                    tree[pwd] = []
                o += 1
            elif f[o][1] == "ls":
                o += 1
                while True:
                    #print("o: ", o)
                    if f[o][0] == "$":
                        break
                    else:
                        tree[pwd].append((f[o][0], f[o][1]))
                        o += 1
                        if o > len(f) - 1:
                            break
        else:
            o += 1
        
        
        #print("Tree: ", tree)
        #print("pwd: ", pwd)
    for k in tree:
        print(k)
        for t in tree[k]:
            print("  ", t)
    return None


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")