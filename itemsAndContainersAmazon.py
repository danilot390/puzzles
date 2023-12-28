def numberOfItems(s,startIndices, endIndices):
    result = []
    for x in range(len(startIndices)):
        a = startIndices[x-1]-1
        b = endIndices[x-1]
        subStr = s[a:b]
        print(a,b)
        print(subStr)
        open = False
        items = 0
        cont = 0
        for char in subStr:
            if open and char == '|':
                items += cont
                cont = 0
            elif char == '|':
                open = True
            if open and char == '*':
                cont += 1
        result.append(items)
    return result

if __name__ == '__main__':
    s='*|***|**|*|'
    startIndices = [1,5]
    endIndices = [7,11]

    result = numberOfItems(s, startIndices, endIndices)

    print(result)