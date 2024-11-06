def longestOnes(nums: list[int], k: int) -> int:
    left = curr = ans = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1

        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


# Test case
# 1
nums_test = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k_test = 2
result = longestOnes(nums_test, k_test)
print(f'max number of consecutive 1\'s is {result}')

# 2
nums_test = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k_test = 3
result = longestOnes(nums_test, k_test)
print(f'max number of consecutive 1\'s is {result}')