from collections import Counter
from heapq import *


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapify(nums)
        while len(nums) > self.k:
            heappop(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        if len(self.nums) != self.k:
            heappush(self.nums, val)
            return self.nums[0]
        if val > self.nums[0]:
            heappush(self.nums, val)
            if len(self.nums) > self.k:
                heappop(self.nums)
        return self.nums[0]




# Test Case
1
ans1 = []
kthLargest = KthLargest(3, [4, 5, 8, 2])
ans1.append(kthLargest.add(3))
ans1.append(kthLargest.add(5))
ans1.append(kthLargest.add(10))
ans1.append(kthLargest.add(9))
ans1.append(kthLargest.add(4))
print(ans1)

# # 2
ans2 = []
kthLargest = KthLargest(2, [0])
ans2.append(kthLargest.add(3))
ans2.append(kthLargest.add(5))
ans2.append(kthLargest.add(10))
ans2.append(kthLargest.add(9))
ans2.append(kthLargest.add(4))
print(ans2)
#
# # 3
ans3 = []
kthLargest = KthLargest(1, [-2])
ans3.append(kthLargest.add(-3))
ans3.append(kthLargest.add(0))
ans3.append(kthLargest.add(2))
ans3.append(kthLargest.add(-1))
ans3.append(kthLargest.add(4))
print(ans3)
#
# # 2
ans4 = []
kthLargest = KthLargest(2, [0])
ans4.append(kthLargest.add(-1))
ans4.append(kthLargest.add(1))
ans4.append(kthLargest.add(-2))
ans4.append(kthLargest.add(-4))
ans4.append(kthLargest.add(3))
print(ans4)

# # 5
ans5 = []
kthLargest = KthLargest(7, [-10,1,3,1,4,10,3,9,4,5,1])
ans5.append(kthLargest.add(3))
ans5.append(kthLargest.add(2))
ans5.append(kthLargest.add(3))
ans5.append(kthLargest.add(1))
ans5.append(kthLargest.add(2))
ans5.append(kthLargest.add(4))
ans5.append(kthLargest.add(5))
ans5.append(kthLargest.add(5))
ans5.append(kthLargest.add(6))
ans5.append(kthLargest.add(7))
ans5.append(kthLargest.add(7))
ans5.append(kthLargest.add(8))
ans5.append(kthLargest.add(2))
ans5.append(kthLargest.add(3))
ans5.append(kthLargest.add(1))
ans5.append(kthLargest.add(1))
ans5.append(kthLargest.add(1))
ans5.append(kthLargest.add(10))
ans5.append(kthLargest.add(11))
ans5.append(kthLargest.add(5))
ans5.append(kthLargest.add(6))
ans5.append(kthLargest.add(2))
ans5.append(kthLargest.add(4))
ans5.append(kthLargest.add(7))
ans5.append(kthLargest.add(8))
ans5.append(kthLargest.add(5))
ans5.append(kthLargest.add(6))
print(ans5)
