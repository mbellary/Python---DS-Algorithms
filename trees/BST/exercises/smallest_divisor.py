import math


import math
def smallestDivisor(nums: list[int], threshold: int) -> int:
    def check(mid):
        sum = 0
        for num in nums:
            sum += math.ceil(num / mid)
        return sum <= threshold

    left = 1
    right = 10 ** 6

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


# Test Case
# 1
nums = [1, 2, 5, 9]
threshold = 6
result = smallestDivisor(nums, threshold)
print(f'smallest divisor is {result}')

# 2
nums = [44,22,33,11,1]
threshold = 5
result = smallestDivisor(nums, threshold)
print(f'smallest divisor is {result}')