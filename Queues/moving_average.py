from collections import deque
import math
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0.

    def next(self, val: int) -> float :
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / self.size


# Test Case
#1
ans = []
obj = MovingAverage(3)
param_1 = obj.next(1)
param_2 = obj.next(10)
param_3 = obj.next(3)
param_4 = obj.next(5)
print(f'{param_4}')