#!/usr/bin/env python3

import random
import os

counter = 0
found = False

def random_list(size):
    list = []
    for i in range(size):
        list.append(random.randint(0, 200))
    return list

def subsetSumSize(A, n, depth, file):
    if depth==0:
        global counter
        counter = counter + 1
    global found
    found = False
    return subsetSumSizeAux(A,0,n,0, depth, file)

def subsetSumSizeAux(A, i, n, sum, depth, file):
    if depth==0:
        global counter
        counter = counter + 1
    with open(file, 'a') as f:
        print("{};{}".format(depth, i), file=f)

    if (i >= n):
        if (sum == 0):
            global found
            found = True
        return 0

    size = subsetSumSizeAux(A,i+1,n,sum + A[i], depth+1, file)
    if (found):
        return size + 1
    size = subsetSumSizeAux(A,i+1,n,sum, depth+1, file)
    return size

def main():
    global counter
    # counter = 0
    size = random.randint(2,10)
    sum = random.randint(1,50)
    arr = random_list(size)
    depth = 0

    path = "./subset_sum"
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    file = "./subset_sum/output-{}".format(size)
    subsetSumSize(arr, size, depth, file)
    with open("./subset_sum/traces", 'a') as f:
        print("{};{}".format(size, counter), file=f)
    counter = 0

if __name__ == '__main__':
    for i in range(20):
        main()
