from functools import cache

def climbStairs(n: int) -> int:
    @cache
    def dp(n):

        if n == 0 or n == 1:
            return 1

        return sum([dp(n - 1) , dp(n - 2)])
    return dp(n)

# Test Case
# 1
n = 2
result = climbStairs(n)
print(f'There are {result} distinct ways to reach to top.')

# 2
n = 3
result = climbStairs(n)
print(f'There are {result} distinct ways to reach to top.')