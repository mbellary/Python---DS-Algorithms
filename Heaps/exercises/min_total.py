import math
from heapq import *

def minStoneSum(piles: list[int], k: int) -> int:

    piles = [-pile for pile in piles]
    heapify(piles)

    while k:
        x = heappop(piles)
        heappush(piles, math.floor( x / 2))
        k -= 1
    return -sum(piles)

# Test Case
# 1
piles = [5,4,9]
k = 2
result = minStoneSum(piles, k)
print(f"the minimum sum is {result}")

# 2
piles = [4,3,6,7]
k = 3
result = minStoneSum(piles, k)
print(f"the minimum sum is {result}")