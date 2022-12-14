#AOC-2022-7-1


import timeit
import time


def numFind(n):
    tree = {}
    pwd = ""
    o = 0
    output = 0
    with open("7.txt") as f:
        f = f.read()
    f = [s.split(" ") for s in f.split("\n")]
    while o < len(f):
        #Start command checking
        if f[o][0] == "$":
            if f[o][1] == "cd":
                if f[o][2] == "..":
                    #removes one dir level depth
                    pwd = pwd[:pwd[:-1].rfind("/") + 1]
                    if pwd == "":
                        pwd = "/"
                else:
                    #creates new absolute path of nested directory
                    pwd = pwd + f[o][2] + "/"
                    #pass
                #prevents double root path
                if pwd[:2] == "//":
                    pwd = pwd[1:]
                #add absolute path to tree dict
                if pwd not in tree:
                    tree[pwd] = []
                o += 1
            elif f[o][1] == "ls":
                o += 1
                while True:
                    if f[o][0] == "$":
                        break
                    else:
                        tree[pwd].append((f[o][0], f[o][1]))
                        allParents = pwd
                        #this loop appends folder values to all parent dirs
                        while len(allParents) > 1:
                            allParents  = allParents[:allParents[:-1].rfind("/") + 1]
                            tree[allParents].append((f[o][0], f[o][1]))
                        ###################################################
                        o += 1
                        if o > len(f) - 1:
                            break
       
    #print tree w/structure
    #for k in tree:
    #    print(k)
    #    for t in tree[k]:
    #        print("  ", t)
    #######################    

    for a in tree:
        dirSizeTotal = 0
        for b in tree[a]:
            if b[0].isnumeric():
                dirSizeTotal += int(b[0])
            elif b[0] == "dir":
                pass
        if dirSizeTotal <= 100000:
            output += dirSizeTotal
    return output


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = 0
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")