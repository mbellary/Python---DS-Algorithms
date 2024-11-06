from functools import cache

def minCostClimbingStairs(cost: list[int]) -> int:

    @cache
    def dp(i):
        if i <= 1:
            return 0

        return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2] )

    return dp(len(cost))

# Test Case
# 1
cost = [10,15,20]
result = minCostClimbingStairs(cost)
print(f'minimum cost of climbing stairs is {result}')

#2
cost = [1,100,1,1,1,100,1,1,100,1]
result = minCostClimbingStairs(cost)
print(f'minimum cost of climbing stairs is {result}')