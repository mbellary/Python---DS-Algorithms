from collections import deque
from heapq import *


def maxSlidingWindow( nums: list[int], k: int) -> list[int]:
    ans = []
    queue = deque()
    for i in range(len(nums)):
        # maintain monotonic decreasing.
        # all elements in the deque smaller than the current one
        # have no chance of being the maximum, so get rid of them
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

        queue.append(i)

        # queue[0] is the index of the maximum element.
        # if queue[0] + k == i, then it is outside the window
        if queue[0] + k == i:
            queue.popleft()

        # only add to the answer once our window has reached size k
        if i >= k - 1:
            ans.append(nums[queue[0]])

    return ans


# Test Case
# 1
x = [1, 3, -1, -3, 5, 3, 6, 7]
res = maxSlidingWindow(x, 3)
print(res)