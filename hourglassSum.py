import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def hourglass(arr,x,y):
    return (arr[x][y]+arr[x][y+1]+arr[x][y+2]+
           arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+
           arr[x+2][y+2])
    
    
def hourglassSum(arr):
    # Write your code here
    startX = 0
    StartY = 0
    highest = -1*sys.maxsize
    
    for i in range(0,4):
        for j in range(0,4):
            current = hourglass(arr,i,j)
            if current > highest:
                highest = current
    
    return highest    

if __name__ == '__main__':
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)