#AOC-2022-11-1


import timeit
import time
from math import prod


tm0 = {"items": [79, 98], "op": " * 19", "mod": 23, "true": "tm2", "false": "tm3", "c": 0}
tm1 = {"items": [54, 65, 75, 74], "op": " + 6", "mod": 19, "true": "tm2", "false": "tm0", "c": 0}
tm2 = {"items": [79, 60, 97], "op": " ** 2", "mod": 13, "true": "tm1", "false": "tm3", "c": 0}
tm3 = {"items": [74], "op": " + 3", "mod": 17, "true": "tm0", "false": "tm1", "c": 0}
tmonkeys = [tm0, tm1, tm2, tm3]

m0 = {"items": [54, 82, 90, 88, 86, 54], "op": " * 7", "mod": 11, "true": "m2", "false": "m6", "c": 0}
m1 = {"items": [91, 65], "op": " * 13", "mod": 5, "true": "m7", "false": "m4", "c": 0}
m2 = {"items": [62, 54, 57, 92, 83, 63, 63], "op": " + 1", "mod": 7, "true": "m1", "false": "m7", "c": 0}
m3 = {"items": [67, 72, 68], "op": " ** 2", "mod": 2, "true": "m0", "false": "m6", "c": 0}
m4 = {"items": [68, 89, 90, 86, 84, 57, 72, 84], "op": " + 7", "mod": 17, "true": "m3", "false": "m5", "c": 0}
m5 = {"items": [79, 83, 64, 58], "op": " + 6", "mod": 13, "true": "m3", "false": "m0", "c": 0}
m6 = {"items": [96, 72, 89, 70, 88], "op": " + 4", "mod": 3, "true": "m1", "false": "m2", "c": 0}
m7 = {"items": [79], "op": " + 8", "mod": 19, "true": "m4", "false": "m5", "c": 0}
monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]


def numFind(n):
    for _ in range(20):
        for mx in n:
            for mi in range(len(mx["items"])): #walks the items list in order
                mx["c"] += 1
                inspect = mx["items"][mi] #gets single item value
                #print("start", inspect)
                inspect = str(inspect) + mx["op"] #bulds equation for worry
                #print("worry op", inspect)
                inspect = eval(inspect) #evaluates worry equation
                #print("new worry", inspect)
                inspect = inspect // 3 #worry divided by 3 and rounded down because monkey didn't dmg item
                #print("relief reduced worry", inspect)
                if inspect % mx["mod"] == 0:
                    #print(True, "Goes to: ", mx["true"])
                    eval(mx["true"])["items"].append(inspect) #adds item to true monkey's list
                else:
                    #print(False, "Goes to: ", mx["false"])
                    eval(mx["false"])["items"].append(inspect) #adds item to false monkey's list
                #print("")
            mx["items"] = [] #empties the current monkey's list
            #print("")
    mb = []
    for mx in n:
        #print("Inspections:", mx["c"], mx["items"])
        mb.append(mx["c"]) #builds the monkey business list
    return prod(sorted(mb)[-2:]) #returns two highest values multiplied together


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = monkeys
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")