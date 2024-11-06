
def minStartValue(nums: list[int]) -> int:

    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])
    n = 10000000
    ans = 0
    for i in range(1, n+1):
        min_vals = [i] * len(nums)
        for j in range(len(min_vals)):
            val = min_vals[j] + prefix[j]
            if val < 1:
                break
            if j == len(prefix) - 1:
                ans = i
        if ans:
            return ans

# Test Case
#1
nums = [-3,2,-3,4,2]
result = minStartValue(nums)
print(result)

#2
nums = [1,2 ]
result = minStartValue(nums)
print(result)

#3
nums = [1,-2,-3]
result = minStartValue(nums)
print(result)

#4
nums = [-22,-29,-21,0,-4,-26,10,-11,-14,-11]
result = minStartValue(nums)
print(result)