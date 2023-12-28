#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Create an empty stack to keep track of open brackets
    stack = []

    # Define a mapping of open and close brackets
    brackets_map = { ')':'(',']':'[','}':'{'}

    # Loop through each character in the input string
    for bracket in s:
        # If the character is a close bracket, check if 
        # it matches the top of the stack
        if bracket in brackets_map.keys():
            # If the stack is empty or the top of the stack doesn't match,
            # the string isn't balanced.  
            if not stack or stack.pop() != brackets_map[bracket]:
                return 'NO'
        # If the character is an open bracket, push it onto the stack
        elif bracket in brackets_map.values():
            stack.append(bracket)
    
    # If the stack is empty at the end, the string is balanced
    return 'YES' if not stack else 'NO'

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        
        print(result)
