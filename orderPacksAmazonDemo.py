from collections import deque

import heapq

# We're going to split the list into "low" and "high" halves.

# The high half will be a MIN heap, the low half will be a MAX heap.
# We'll pop one into the other as needed to keep them close in size.

# Then low[0] & high[0] will always return middle values of the list.

# In order to implement a max heap with heapq, we just fill it with
# negative numbers. So we'll invert numbers we push into low, and
# re-invert numbers we pop out of it.
def minimalHeaviestSetA(a):
    low = []    # Lower half of the input
    high = []   # Upper half of the input

    for i in range(len(a)):
        # First, sort the list value into the correct half.
        # We'll prioritize high to minimize negative inversion.

        if i == 0 or a[i] >= med:
            heapq.heappush(high, a[i])
        else:
            heapq.heappush(low, a[i] * -1)

        # Now make sure the halves are equally sized. Since high
        # is filled first, it can be one element longer than low.
        # Otherwise they must have equal lengths.

        if len(high) - len(low) > 1:
            heapq.heappush(low, heapq.heappop(high) * -1)
        elif len(low) > len(high):
            heapq.heappush(high, heapq.heappop(low) * -1)

        # Rest of the logic is easy. If high is longer than low,
        # there's an odd number of elements in the list, and the
        # middle value is the bottom of high. Otherwise, there's
        # an even number of elements in the list, so the median
        # is half the sum of each half's 0th element. Since low is
        # stored negative, we'll just subtract it to find the sum.

        if len(high) > len(low):
            med = float(high[0])
        else:
            med = float((high[0] - low[0]) / 2)
    while len(high)>=len(low):
        heapq.heappush(low, heapq.heappop(high) * -1)
    print(high[0],low[0])
    while True:
        if high[0] == -1*low[0]:
            heapq.heappush(low, heapq.heappop(high) * -1)
        else:
            break

    return high,low
if __name__ == '__main__':
    array = [1,3,7,5,6,2,1,8,6,6,6,40] 

    result = minimalHeaviestSetA(array)

    print(result)