#AOC-2022-16-1


import timeit
import time
from copy import deepcopy


def numFind():
    valve_info = {}
    valve_state = {}
    #paths = [['AA']]
    paths = [['AA', 'DD', 'CC'], ['AA', 'DD', 'AA'], ['AA', 'DD', 'EE'], ['AA', 'II', 'AA'], ['AA', 'II', 'JJ'], ['AA', 'BB', 'CC'], ['AA', 'BB', 'AA']]
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
        valve_info[v[0]] = {"flow": int(v[1]), "leads": v[2:]} #builds the valve_info dict with attributes
        valve_state[v[0]] = False #builds the valve_state dict with state

    #for v, vi, vs in zip(valve_state, valve_info.values(), valve_state.values()):
    #    print(v, vi, vs)
    
    #print(valve_info['AA'], valve_state['AA'])
    steps = 2

    while steps < 30:
        new_paths = []
        for path in paths:
            if len(set(path)) == 2:
                continue
            else:
                cur_pos = path[-1]
                for next_step in valve_info[cur_pos]["leads"]:
                    new_paths.append(path + [next_step])
        paths = deepcopy(new_paths)
        print("Step:", steps, "Num of Paths:", len(paths))
        steps += 1
    #print("All Paths:", paths)
    print("path len:", len(paths[5]))
    return list(valve_state.values()).count(False) #use this in the while loop to detect if all valves are open
    






if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print('*******WIP*********')
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")