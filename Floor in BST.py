class Solution:
    def floor(self, root, x):
        if root is None:
            return -1
        
        # Initial "floor" as -1
        floor_val = -1
        
        while root:
            if root.data == x:
                # If we find the exact value, the "floor" is that value
                return root.data
            elif root.data > x:
                # If the value in the current node is greater than x, it cannot be the "floor".
                root = root.left
            else:
                # If the value in the current node is less than or equal to x, 
                # update the "floor" and continue searching to the right.
                floor_val = root.data
                root = root.right
        
        return floor_val

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))