import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
class bTree:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
        self.children = 0
    
    def insert(self, val):
        if not self.val:
            self.val = val
            return 
        
        if val < self.val:
            self.children += 1
            if self.left:
                self.left.insert(val)
                return            
            self.left = bTree(val)
            return
        
        if self.right:
            self.left = bTree(-1)
            self.right.insert(val)
            return
        self.right = bTree(val)

    def brives(self, cont=0):
        if self.left is not None:
            self.left.brives(cont)
        if self.val is not None:
            print(self.val,self.children)
        if self.right is not None:
            self.right.brives(cont)
        return cont
    
def minimumBribes(q):
    queue = bTree()
    for person in q:
        queue.insert(person)
    
    queue.brives()


    # Write your code here
    # bribes = 0
    # differentePosition = 0
    # people=set(q)
    # print(people)
    # for i in range(0,len(q)):
    #     current = q[i]
    #     print(current)
    #     position = i+1+differentePosition
        
    #     if current > position:
    #         print(current,position, current - position)
    #     #    if current - position > 2:
    #     #        print('Too chaotic')
    #     #        return
    #         bribes += current-position
    #     #    differentePosition += current-position
    # print(f'brives->{bribes}')
    return

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))
        print('______*_____')
        minimumBribes(q)
