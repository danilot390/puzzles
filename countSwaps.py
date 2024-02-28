#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
def isSorted(array):
    for i in range(1,len(array)):
        if array[i-1] > array[i]:
            return False
    return True

def countSwaps(a):
    first = min(a)
    last = max(a)
    swaps = 0
    while(isSorted(a)==False):
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j] > a[j+1]:
                    aux = a[j]
                    a[j] = a[j+1]
                    a[j+1] = aux
                    swaps += 1
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {first}')
    print(f'Last Element: {last}')
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
