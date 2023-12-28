#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#
def countA(string):
    count = 0
    for char in string:
        if char == 'a':
            count+=1
    return count
def repeatedString(s, n):
    # Write your code here
    wordLoops = int(n/len(s))
    charsLoops = n%len(s)
    count = (wordLoops*countA(s))+ countA(s[:charsLoops])
    
    return count
    
    

if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)
