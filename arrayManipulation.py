#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Initialize an array of zeros with size n+1
    array = [0] * (n + 1)
    
    # Initialize variables for tracking maximum and current sum
    maximum = 0
    current_sum = 0

    # Iterate through each query and apply updates to the array
    for query in queries:
        start_index = query[0] - 1
        end_index = query[1]
        value = query[2]

        #update start index with the given value
        array[start_index] += value

        # Update end index +1 with the negative of the value
        array[end_index] -= value
    
    # Iterate through the updated array to calculate the
    # maximun value
    for value in array:
        current_sum += value
        maximum = max(maximum, current_sum)

    # Return the maximum value
    return maximum
            

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)