import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#


def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    
    result = [[0 for _ in range(n)] for _ in range(m)]
    resul = sys.stdout
    lenMat = int(m/2) if m%2==0 else int(m/2)+1
    for i in range(lenMat):
        aux1 = [0+i,m-i,0+i,n-i]
        aux2 = [0+i,m-i,0+i,n-i]
        values=[]
        loop = ((aux1[1]-aux1[0])*2)+((aux1[3]-aux1[2]-2)*2)
        mov = True
        for _ in range (loop):
            values.append([aux1[0],aux1[2]])
            if mov and aux1[0] < aux2[1]-1:
                aux1[0]+=1
            elif mov and aux1[0] == aux2[1]-1 and aux1[2]<aux2[3]-1:
                aux1[2]+=1
            elif mov and aux1[0] == aux2[1]-1 and aux1[2] == aux2[3]-1:            
                mov = False
            if (mov is False) and (aux1[0]>aux2[0]):
                aux1[0] -= 1
            elif mov is False:
                aux1[2] -= 1
        cant = r
        lenVal = len(values)

        for i in range(lenVal):
            x,y = values[i]
            nextVal = i+cant
            while nextVal >= lenVal:
                nextVal-= lenVal
            
            xx,yy = values[nextVal]
            result[xx][yy] = matrix[x][y]
    for x in result:
        for y in x:
            resul.write(str(y)+' ')
        resul.write('\n')

    return resul

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))
    print('________________***______________________')
    print(matrixRotation(matrix, r))