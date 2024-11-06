from functools import cache

def maxProfit(prices: list[int], fee: int) -> int:

    @cache
    def dp(i, holding):

        if i == len(prices):
            return 0

        ans = dp(i + 1, holding)

        if holding:
            ans = max(ans, prices[i] + dp(i + 1, False) - fee)
        else:
            ans = max(ans, -prices[i] + dp(i + 1, True))

        return ans
    return dp(0, False)

# Test Case
#1
prices = [1,3,2,8,4,9]
fee = 2
result = maxProfit(prices, fee)
print(f'max profit is {result}')

#2
prices = [1,3,7,5,10,3]
fee = 3
result = maxProfit(prices, fee)
print(f'max profit is {result}')
