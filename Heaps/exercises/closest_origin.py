import math
from heapq import *
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    origin = [0, 0]
    heap = []
    for x, y in points:
        distance = math.sqrt((x - origin[0])**2 + (y - origin[0])**2)
        heappush(heap, (-distance, x, y))
        if len(heap) > k:
            heappop(heap)
    return [[triplet[1], triplet[2]]  for triplet in heap]


# Test Case
# 1
points = [[1,3],[-2,2]]
k = 1
result = kClosest(points, k)
print(f'closest point to origin is {result}')

# 2
points = [[3,3],[5,-1],[-2,4]]
k = 2
result = kClosest(points, k)
print(f'closest point to origin is {result}')