#User function Template for python3
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def dupSub(self, root):
        # Helper function to perform in-order traversal and store subtrees
        def in_order_traversal(node, subtrees):
            if not node:
                return 'N'  # Representing null nodes with 'N'

            # Serialize the left subtree
            left_str = in_order_traversal(node.left, subtrees)

            # Serialize the current node
            current_str = str(node.data)

            # Serialize the right subtree
            right_str = in_order_traversal(node.right, subtrees)

            # Create a serialized representation of the current subtree
            subtree_str = left_str + current_str + right_str

            # Check if the subtree has been seen before (accounting for duplicate values)
            if subtree_str in subtrees or subtree_str.count(current_str) > 2:
                return 'D'  # Representing a duplicate subtree with 'D'

            # Add the current subtree to the set of seen subtrees
            subtrees.add(subtree_str)

            print(subtrees)
            print(subtree_str)
            return subtree_str

        # Set to store serialized representations of subtrees
        subtrees = set()

        # Perform the in-order traversal and check for duplicate subtrees
        result = in_order_traversal(root, subtrees)

        # If a 'D' is present, it indicates a duplicate subtree
        return '1' if 'D' in result else '0'

#{ 
# Driver Code Starts
#Initial Template for Python 3
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.dupSub(root))
# } Driver Code Ends