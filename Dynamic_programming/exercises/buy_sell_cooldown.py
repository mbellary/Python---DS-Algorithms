from functools import cache

def maxProfit(prices: list[int]) -> int:

    @cache
    def dp(i, holding, cooldown):

        if i == len(prices):
            return 0

        if cooldown:
            return i - 2

        ans = dp(i + 1, holding, cooldown)

        if holding:
            ans = max(ans, prices[i] + dp( i + 1, False, True))
        else:
            ans = max(ans, -prices[i] + dp(i + 1, True, False))
        return ans
    return dp(0, False, False)

# Test Case
#1
prices = [1,2,3,0,2]
result = maxProfit(prices)
print(f'max profit is {result}')

#2
prices = [1]
result = maxProfit(prices)
print(f'max profit is {result}')

#2
prices = [1, 4, 2]
result = maxProfit(prices)
print(f'max profit is {result}')