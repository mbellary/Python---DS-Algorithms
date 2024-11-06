from heapq import *

def connectSticks(sticks: list[int]) -> int:

    sticks = [stick for stick in sticks]
    heapify(sticks)
    cost = 0

    while len(sticks) > 1:
        first = heappop(sticks)
        second = heappop(sticks)
        heappush(sticks, first + second)
        cost += first + second
    return cost

# Test Case
#1
sticks = [2,4,3]
result = connectSticks(sticks)
print(f'The minimum cost to connect {result}')

# 2
sticks = [1,8,3,5]
result = connectSticks(sticks)
print(f'The minimum cost to connect {result}')

# 3
sticks = [5]
result = connectSticks(sticks)
print(f'The minimum cost to connect {result}')