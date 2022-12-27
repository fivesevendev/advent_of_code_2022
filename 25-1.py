#AOC-2022-25-1


import timeit
import time
from copy import deepcopy

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
    built = False
    while sN > 0:
        for five in range(len(fives)):
            if fives[five] > sN:
                fiv = deepcopy(fives[five - 1]) #picks value below the too big value of power of 5
                #print("sN:", sN, "fiv:", fiv)
                break
        
        if sN / fiv > 2:
            fiv = deepcopy(fives[fives.index(fiv) + 1]) #if it requires more than 2 of this value it much require a larger value power of 5
            five += 1 #adjust the fives mult value position
        
        if not built:
            print("building")
            output = list(str(fiv // sN) + str("0" * (five - 1)))
            built = True
        else:
            print("built")
            if current_num > target:
                #pass #build here for negatives
                if fiv // sN == 2:
                    output[position] = "="
                elif fiv // sN == 1:
                    output[position] = "-"
                else:
                    output[position] = "0"
            else:
                output[position] = str(fiv // sN)
        position += 1
        current_num = unSnafu(output)
        print("target:", target, "sN:", sN, "current:", current_num, "output:", "fiv:", fiv, "output", output)
        sN = fiv % sN
        
        time.sleep(5)

    print(output)


def sBuilder():
    pass

if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", numFind())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")