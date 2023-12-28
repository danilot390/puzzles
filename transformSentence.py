#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here

    newStr = sentence[0]
    prev = sentence[0]
    alphabet_map = {'A' :    1,'a' :    1,'B' :     2,'b' :    2,'C' :     3,'c' :    3,'D' :     4,'d' :    4,'E' :     5,'e' :    5,'F' :     6,'f' :    6,'G' :     7,'g' :    7,'H' :     8,'h' :    8,'I' :     9,'i' :    9,'J' :     10,'j' :    10,'K' :     11,'k' :    11,'L' :     12,'l' :    12,'M' :     13,'m' :    13,'N' :     14,'n' :    14,'O' :     15,'o' :    15,'P' :     16,'p' :    16,'Q' :     17,'q' :    17,'R' :     18,'r' :    18,'S' :     19,'s' :    19,'T' :     20,'t' :    20,'U' :     21,'u' :    21,'V' :     22,'v' :    22,'W' :     23,'w' :    23,'X' :     24,'x' :    24,'Y' :     25,'y' :    25,'Z' :     26,'z' :    26,' ':99}
    
    for x in range(1,len(sentence)):
        
        char = sentence[x]
        
        print(prev)
        
        if char == ' ':
            newStr += ' '
        elif prev == ' ':
            newStr += char
        elif alphabet_map[prev] < alphabet_map[char]:
            newStr += char.upper()
        elif alphabet_map[char] < alphabet_map[prev]:
            newStr += char.lower()
        elif alphabet_map[char] == alphabet_map[prev]:
            newStr += char
            
        prev = char

    return newStr

if __name__ == '__main__':
    sentence = input()

    result = transformSentence(sentence)

    print(result)
