#!/usr/bin/env python3

import random
import os

counter = 0

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        # self.insert(random.randint(2,50))

    def insert(self, data):
        if self.data:
            # if data < self.data:
            if size(self.left) < size(self.right):
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # elif data > self.data:
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        assert(abs(size(self.right)-size(self.left)) <= 1)

    def populate(self, size):
        for i in range(size):
            val = random.randint(-size, size)
            self.insert(val)
        return

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left) + 1 + size(node.right))

# Recursive function to perform postorder traversal on the tree
def postorder(root, depth, file):
    with open(file, 'a') as f:
        print("{};{}".format(depth, size(root)), file=f)
    if depth==0:
        global counter
        counter = counter + 1

    if root is None:
        return
    postorder(root.left, depth+1, file)
    postorder(root.right, depth+1, file)
    # print(root.data, end=' ')

# Recursive function to perform inorder traversal on the tree
def inorder(root, depth, file):
    with open(file, 'a') as f:
        print("{};{}".format(depth, size(root)), file=f)
    if depth==0:
        global counter
        counter = counter + 1

    if root is None:
        return
    inorder(root.left, depth+1, file)
    # print(root.data, end=' ')
    inorder(root.right, depth+1, file)

# Recursive function to perform inorder traversal on the tree
def copy(root, depth, file):
    with open(file, 'a') as f:
        print("{};{}".format(depth, size(root)), file=f)
    if depth==0:
        global counter
        counter = counter + 1

    if root is None:
        return
    # if root.left:
    copy(root.left, depth+1, file)
    # if root.right:
    copy(root.right, depth+1, file)

# Driver collect traces
def main():
    global counter
    counter = 0
    depth = 0
    root = Node(random.randint(-10,10))
    root.populate(random.randint(2,500))
    siz = size(root)

    path = "./postorder"
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    file = "./postorder/output-{}".format(siz)
    postorder(root, depth, file)
    with open("./postorder/traces", 'a') as f:
        print("{};{}".format(siz, counter), file=f)
    counter = 0

    path = "./inorder"
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    file = "./inorder/output-{}".format(siz)
    inorder(root, depth, file)
    with open("./inorder/traces", 'a') as f:
        print("{};{}".format(siz, counter), file=f)
    counter = 0

    path = "./bstcopy"
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    file = "./bstcopy/output-{}".format(siz)
    copy(root, depth, file)
    with open("./bstcopy/traces", 'a') as f:
        print("{};{}".format(siz, counter), file=f)
    counter = 0


if __name__ == '__main__':
    for i in range(100):
       main()
