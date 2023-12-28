
import math
import os
import random
import re
import sys


# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries

from collections import deque
class BTNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

    def build(self, indexes):
        queue = deque([self])

        curr_ind = 0

        while queue:
            curr_node = queue.popleft()

            if curr_node.val != -1:
                left, right = indexes[curr_ind]
                curr_ind += 1

                curr_node.left = BTNode(left)
                curr_node.right = BTNode(right)

                queue.append(curr_node.left)
                queue.append(curr_node.right) 
        
        return curr_node
    
    def inorder_transversal(self):
        if self is not None:
            if self.left:
                self.left.inorder_transversal()
            if self.val != -1:
                print(self.val)
            if self.right:
                self.right.inorder_transversal()

    def swap(self, depth,result, level=1):
        if not self:
            return
        if depth == level:
            print(level, self.val)
            left = self.left
            self.left = self.right
            self.right = left
        level += 1
        if self.left:
            self.left.swap(depth,result,level)
        if self.val != -1:
            result.append(self.val)
        if self.right:
            self.right.swap(depth,result,level)

        return result

def swapNodes(indexes, queries):
        
    root = BTNode(1)
    root.build(indexes)
    result = []
    newLimit = len(indexes)+10
    sys.setrecursionlimit(newLimit)
    for k in queries:
        result.append(root.swap(k,[]))

    return result

if __name__ == '__main__':


    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    print(swapNodes(indexes, queries))
