def max_avg_subarray(nums: list, k: int) -> float:
    curr = ans = 0
    for i in range(k):
        curr += nums[i]

    curr /= k
    ans = curr
    for i in range(k, len(nums)):
        curr += (nums[i] - nums[i - k]) / k
        ans = max(ans, curr)

    return ans


# Test Case
# 1
nums_test = [1, 12, -5, -6, 50, 3]
k_test = 4
result = max_avg_subarray(nums_test, k_test)
print(f'max average value of the subarray {result}')

# 2
nums_test = [5]
k_test = 1
result = max_avg_subarray(nums_test, k_test)
print(f'max average value of the subarray {result}')

# 3
nums_test = [3, 3, 4, 3, 0]
k_test = 3
result = max_avg_subarray(nums_test, k_test)
print(f'max average value of the subarray {result}')