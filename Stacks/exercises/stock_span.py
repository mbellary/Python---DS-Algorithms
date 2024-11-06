from collections import deque


class StockSpanner:

    def __init__(self, nums: list[int]):
        self.stack = nums
    def next(self, price: int) -> int:
        hist = []
        while self.stack and self.stack[-1] >= price:
            hist.append(self.stack.pop())
        self.stack.append(price)
        days = len(self.stack)
        self.stack = hist + self.stack
        print(self.stack)

        return days

# Test Case
# 1
ans = []
stockSpanner = StockSpanner([]);
ans.append(stockSpanner.next(100))
ans.append(stockSpanner.next(80))
ans.append(stockSpanner.next(60))
ans.append(stockSpanner.next(70))
ans.append(stockSpanner.next(60))
ans.append(stockSpanner.next(75))
ans.append(stockSpanner.next(85))
print(ans)
