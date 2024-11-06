def check_for_target(nums: list, target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]

        if curr == target:
            return True

        if curr > target:
            right -= 1
        else:
            left += 1
    return False


# Test Cases
# 1 found the target
k = 13
arr = [1, 2, 4, 6, 8, 9, 14, 15]
result = check_for_target(arr, k)

if result:
    print(f'#1 Found the pair')

# 2 Match not found

k = 100
arr = [1, 2, 4, 6, 8, 9, 14, 15]
result = check_for_target(arr, k)

if result:
    print(f'#1 No Match was found!')