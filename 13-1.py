#AOC-2022-13-1


import timeit
import time


def numFind():
    correctOrder = []
    with open("13.txt") as f:
        f = f.read()
    f = [s for s in f.split("\n")]
    pPairs = {}
    count = 1
    for x in f:
        if x != "":
            pPairs[count] = eval(x) #add number entries of list(s) to dict
            count += 1
    #print(pPairs)
    for p in range(1, len(pPairs), 2):
        print("Pair Index: ", (p + 1) // 2)
        inOrder = True
        l = pPairs[p]
        r = pPairs[p + 1]
        #print(l, "v", r)
        print("l: {} v {} :r = {}".format(type(l), type(r), listComp(l, r)))

    return "*****WIP*****"
    return correctOrder
    
def intComp(l, r):
    print(l, "<=", r, l <= r)
    return l <= r

def listComp(l, r):
    if len(l) == len(r):
        for ll, rr in zip(l, r):
            #print(ll, type(ll), type(rr))
            while type(ll) == list:
                try:
                    ll = ll[0]
                except IndexError:
                    return True
            while type(rr) == list:
                try:
                    rr = rr[0]
                except IndexError:
                    return False
            
            if ll > rr:
                return False
        else:
            print("else true")
            return True
    return len(l) < len(r)

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")