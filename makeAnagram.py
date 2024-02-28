#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def len_intersection(array1, array2):
    array_comp = [char for char in array2]
    len_inter = 0
    for i in array1:
        if i in array_comp:
            array_comp.remove(i)
            len_inter +=1
    return len_inter


def makeAnagram(a, b):
    len_inter = len_intersection(a, b)
    
    count_delete = (len(a)-len_inter)+(len(b)-len_inter)
    
    return count_delete

if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)


