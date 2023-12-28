def checkMagazine(magazine, note):
    # Prepare the initial variables
    magazine = set(magazine)
    result = 'Yes'
    
    
    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            result = 'No'
    print(result)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)