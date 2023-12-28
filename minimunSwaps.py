# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    dic = {arr[i]:i for i in range(len(arr))}
    swaps = 0
    for i in range(len(arr)):
        current = arr[i]
        positition = i+1
        if positition != current:
            arr[dic[positition]] = current
            dic[current] = dic[positition]
            arr[i]=positition
            swaps += 1
    return swaps

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)