import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
def magazineToDict(magazine):
    result = {}
    for word in magazine:
        try:
            result[word] += 1
        except:
            result[word] = 1
    return result
def checkMagazine(magazine, note):
    # Prepare the initial variables
    result = 'Yes'
    magazine = magazineToDict(magazine)
    
    for word in note:
        try:
            if magazine[word] > 1:
                magazine[word] -= 1
            else:
                magazine.pop(word)
        except:
            result='No'
            break
            
    print(result)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
