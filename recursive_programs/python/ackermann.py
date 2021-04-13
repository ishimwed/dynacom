#!/usr/bin/env python3

import os
import sys
import random
counter = 0

def ackermann(m, n, file, depth, s ="% s"):
    # print(s % ("A(% d, % d)" % (m, n)))
    with open(file, 'a') as f:
        print("{};{}".format(depth, m), file=f)
    if depth==0:
        global counter
        counter = counter + 1

    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1, file, depth+1, s)
    n2 = ackermann(m, n - 1, file, depth+1, s % ("A(% d, %% s)" % (m - 1)) )
    return ackermann(m - 1, n2, file, depth+1 , s)

if __name__ == '__main__':
    sys.setrecursionlimit(14000)
    for i in range(1):
        n = random.randint(5,20)
        m = random.randint(5,20)
        depth = 0
        path = "./ackermann"
        try:
            os.mkdir(path)
        except OSError as error:
            pass
        file = "./ackermann/output-{}".format(n)
        ackermann(m, n, file, depth)
        with open("./ackermann/traces", 'a') as f:
            print("{};{}".format(n, counter), file=f)
        counter = 0
