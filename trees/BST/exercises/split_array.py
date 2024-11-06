def splitArray(nums: list[int], k: int) -> int:
    def check(mid):
        left_bound = nums[:mid+1]
        right_bound = nums[mid+1:]

        if sum(left_bound) > sum(right_bound) and len(left_bound) >= len(right_bound):
            return sum(left_bound)
        else:
            return sum(right_bound)

    left = 1
    right = max(nums)

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

# Test Case
#1
nums = [7,2,5,10,8]
k = 2
result = splitArray(nums, k)
print(f'{result}')