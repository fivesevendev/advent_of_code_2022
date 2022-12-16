#AOC-2022-16-1


import timeit
import time


def numFind():
    valves = {}
    seconds = 30
    with open("16.txt") as f:
        f = f.read()
    f = [s for s in f.split("\n")]
    for ff in range(len(f)):    
        f[ff] = f[ff].replace("Valve", "")
        f[ff] = f[ff].replace("has flow rate=", ",")
        f[ff] = f[ff].replace("els", "el").replace("ads", "ad").replace("ves", "ve")
        f[ff] = f[ff].replace("; tunnel lead to valve", ",")
        f[ff] = f[ff].replace(" ", "")
    
    for vf in f:
        v = vf.split(",")
        valves[v[0]] = {"flow": int(v[1]), "leads": v[2:], "open": False} #builds the valves dict with attributes
    
    while seconds > 0:
        break

    return "*****WIP*****"
    

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")