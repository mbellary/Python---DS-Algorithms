def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        num = nums[mid]

        if num == target:
            return mid

        if num > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


# Test Case
# 1
nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(f'{result}')

# 2
nums = [1, 3, 5, 6]
target = 2
result = searchInsert(nums, target)
print(f'{result}')

# 3
nums = [1, 3, 5, 6]
target = 7
result = searchInsert(nums, target)
print(f'{result}')