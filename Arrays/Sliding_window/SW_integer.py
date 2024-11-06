def find_length(nums: list, k: int) -> int:
    left = curr = ans = 0

    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)

    return ans


# Test Case
# 1
nums_test = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
result = find_length(nums_test, k)
print(f'Length of the longest subarray is {result}')
