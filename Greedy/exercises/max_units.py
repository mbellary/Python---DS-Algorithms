from collections import defaultdict
from heapq import *

def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:

    counts = defaultdict(int)
    heap = []

    for b, u in boxTypes:
        counts[u] += b

    for units, types in counts.items():
        heappush(heap, (-units, types))

    max_units = 0
    remaining = truckSize
    while remaining:
        units, boxtypes = heappop(heap)
        if boxtypes > remaining:
            boxtypes = remaining
        remaining -= boxtypes
        max_units += (units * boxtypes)
        if not heap:
            return -max_units
    return -max_units




#Test Case
#1
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
result = maximumUnits(boxTypes, truckSize)
print(result)

# 2
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
result = maximumUnits(boxTypes, truckSize)
print(result)

#3
boxTypes = [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]]
truckSize = 13
result = maximumUnits(boxTypes, truckSize)
print(result)

#4
boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35
result = maximumUnits(boxTypes, truckSize)
print(result)

