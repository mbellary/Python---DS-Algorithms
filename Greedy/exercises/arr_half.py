from collections import Counter
from heapq import *


def minSetSize(arr: list[int]) -> int:
    counts = Counter(arr)
    arr_size = len(arr) // 2
    heap = []

    for k, v in counts.items():
        heappush(heap, (-v, k))

    value = 0
    ans = []
    while value < arr_size:
        v, k = heappop(heap)
        value -= v
        ans.append(k)

    return len(ans)

#Test Case
# 1
arr = [3,3,3,3,5,5,5,2,2,7]
result = minSetSize(arr)
print(result)

# 2
arr = [7,7,7,7,7,7]
result = minSetSize(arr)
print(result)