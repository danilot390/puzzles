#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumTimeSpent' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY comedyReleaseTime
#  2. INTEGER_ARRAY comedyDuration
#  3. INTEGER_ARRAY dramaReleaseTime
#  4. INTEGER_ARRAY dramaDuration
#

def minimumTimeSpent(comedyReleaseTime, comedyDuration, dramaReleaseTime, dramaDuration):
    max = len(comedyDuration) if len(comedyDuration)>len(dramaDuration) else len(dramaDuration)
    print(max)
    first= [sys.maxsize,sys.maxsize]
    second= [sys.maxsize,sys.maxsize]
    #First movie
    for i in range(max):        
        if comedyReleaseTime[i]:
            if comedyReleaseTime[i]+comedyDuration[i] < first[1]:
                first = [comedyReleaseTime[i], comedyReleaseTime[i]+comedyDuration[i]]
        if dramaDuration[i]:
                if dramaReleaseTime[i]+dramaDuration[i] < first[1]:
                    first = [dramaReleaseTime[i], dramaReleaseTime[i]+dramaDuration[i]]
    #Second movie
    for i in range(max):        
        if comedyReleaseTime[i]>= first[1] and comedyReleaseTime[i]+comedyDuration[i]<second[1]:
            second = [comedyReleaseTime[i], comedyReleaseTime[i]+comedyDuration[i]]
        if dramaReleaseTime[i]>= first[1] and dramaReleaseTime[i]+dramaReleaseTime[i] < second[1]:
            second = [comedyReleaseTime[i], comedyReleaseTime[i]+comedyDuration[i]]
            
    print(first)                       
    print(second)
    return second[1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    comedyReleaseTime_count = int(input().strip())

    comedyReleaseTime = []

    for _ in range(comedyReleaseTime_count):
        comedyReleaseTime_item = int(input().strip())
        comedyReleaseTime.append(comedyReleaseTime_item)

    comedyDuration_count = int(input().strip())

    comedyDuration = []

    for _ in range(comedyDuration_count):
        comedyDuration_item = int(input().strip())
        comedyDuration.append(comedyDuration_item)

    dramaReleaseTime_count = int(input().strip())

    dramaReleaseTime = []

    for _ in range(dramaReleaseTime_count):
        dramaReleaseTime_item = int(input().strip())
        dramaReleaseTime.append(dramaReleaseTime_item)

    dramaDuration_count = int(input().strip())

    dramaDuration = []

    for _ in range(dramaDuration_count):
        dramaDuration_item = int(input().strip())
        dramaDuration.append(dramaDuration_item)

    result = minimumTimeSpent(comedyReleaseTime, comedyDuration, dramaReleaseTime, dramaDuration)

    fptr.write(str(result) + '\n')

    fptr.close()
