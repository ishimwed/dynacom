#!/usr/bin/env python3

import random
import os
counter = 0

def copy(t_height, file, depth):
    with open(file, 'a') as f:
        print("{};{}".format(depth, (t_height)), file=f)
    if depth==0:
        global counter
        counter = counter + 1

    lc_height = random.randint(-1, t_height )
    rc_height = random.randint(-1, t_height )

    #assume t_height == lc_height + 1 or t_height == rc_height + 1
    if not(t_height == lc_height + 1 or t_height == rc_height + 1):
        flip = random.randint(0, 3 )
        if (flip==0):
            lc_height = t_height - 1
        elif (flip==1):
            rc_height = t_height - 1
        else:
            lc_height = t_height - 1
            rc_height = t_height - 1


    if (lc_height >= 0):
         copy(lc_height, file, depth+1)
    if (rc_height >= 0):
         copy(rc_height,file, depth+1)


if __name__ == '__main__':
    for i in range(10):
        n = random.randint(5,20)
        depth = 0
        path = "./copy"
        try:
            os.mkdir(path)
        except OSError as error:
            pass
        file = "./copy/output-{}".format(n)
        copy(n, file, depth)
        with open("./copy/traces", 'a') as f:
            print("{};{}".format(n, counter), file=f)
        counter = 0
