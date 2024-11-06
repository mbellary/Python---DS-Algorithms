def numSubarrayProductLessThanK(nums: list, k: int) -> int:
    left = ans = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1
    return ans


# Test Case
# 1
nums_test = [10, 5, 2, 6]
k_test = 100
result = numSubarrayProductLessThanK(nums_test, k_test)
print(f'total number of subarrays {result}')
