def sum_fixed_window(nums: list, k: int) -> int:
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]
        ans = max(ans, curr)
    return ans


# Test Case
#1
nums_test = [3, -1, 4, 12, -8, 5, 6]
k_test = 4
result = sum_fixed_window(nums_test, k_test)

print(f'Largest sum of a subarray {result}')