#AOC-2022-25-1


import timeit
import time
from copy import deepcopy
import sys

sKey = {"2": 2, "1":1, "0":0, "-":-1, "=":-2}
fives = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 30517578125, 152587890625, 762939453125, 3814697265625, 19073486328125, 95367431640625, 476837158203125, 2384185791015625, 11920928955078125, 59604644775390625]

decimal_answer = 30223327868980

def numFind():
    with open("25.txt") as f:
        f = f.read()
    f = [list(s) for s in f.splitlines()]
    total = 0
    for ef in f:
        total += unSnafu(ef)
    #return total
    #print(total)
    #return snafu(total)
    print(snafu(1747))

def unSnafu(u_sN):
    output = 0
    for u, v in list(enumerate(u_sN[::-1])):
        output += ((5 ** u) * sKey[v]) #turns snafu number into decimal number
    return output


def snafu(sN):
    target = int(sN)
    current_num = 0
    position = 0
    for five in range(len(fives)):
        if ((fives[five] * 2) % sN) < (fives[five] // 2):
            #print(fives[five])
            #sys.exit()
            #fiv = deepcopy(fives[five])
            working_range = deepcopy(fives[:five + 1])[::-1] #use working range to pick values for slots
            #fiv = deepcopy(fives[five - 1]) #picks value below the too big value of power of 5
            #if sN / fiv > 2:
            #    fiv = deepcopy(fives[fives.index(fiv) + 1]) #if it requires more than 2 of this value it much require a larger value power of 5
            #    five += 1 #adjust the fives mult value position
            print("building")
            output = list(str("0" * (five)))
            output[position] = fives[five] // sN
            sN = fives[five] % sN
            position += 1
            break    
    #print("five:", five)
    #print("working_range:", working_range)
    

    for slot in working_range:
        if slot > target:
            print("slot > target")
            if current_num > sN:
                if slot // sN == 2:
                    output[position] = "="
                elif slot // sN == 1:
                    output[position] = "-"
                else:
                    print("size:", slot // sN)
            else:
                print("else")
                output[position] = str(slot // sN)
        sN = sN % slot
        print("target:", target, "sN:", sN, "current:", current_num, "slot:", slot, "output", output)

        position += 1
        current_num = unSnafu(output)
        
        
        time.sleep(5)




if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")