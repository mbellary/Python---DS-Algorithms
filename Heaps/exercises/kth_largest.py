from heapq import *
from collections import Counter

def findKthLargest( nums: list[int], k: int) -> int:

    heapify(nums)
    while len(nums) > k:
        heappop(nums)
    return nums[0]

# Test Case
# 1
nums = [3,2,1,5,6,4]
k = 2
result = findKthLargest(nums, k)
print(f'The kth largest num {result}')

# 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
result = findKthLargest(nums, k)
print(f'The kth largest num {result}')


