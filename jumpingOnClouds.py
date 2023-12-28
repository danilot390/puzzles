def jumpingOnClouds(c):
    # Write your code here
    i=0
    cont = 0
    size = len(c)

    while i < size-1:
        if i+2 < size and c[i+2] != 1:
            i += 2
        else:
            i += 1
        cont+=1
    return cont

if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
