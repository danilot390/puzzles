class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

from collections import deque
def levelOrder(root):
    if not root:
        return
    
    # Create an empty list to store node values as string
    result = []

    # Create a deque(Double-ended queue) to store nodes for traversal
    queue = deque([root])
    cont = 1
    while queue:
        # Remove the leftmost node from the  queue
        node = queue.popleft()

        # append the value of the node to the result list
        result.append(str(node.info))

        #if a left child exist, add it to the queue
        if node.left:
            queue.append(node.left)
        
        # If a right child exist, add it to the queue
        if node.right:
            queue.append(node.right)

    # Join the result list into a single string and print it
    print(' '.join(result))


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])
levelOrder(tree.root)
