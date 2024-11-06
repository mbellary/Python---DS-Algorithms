def missing_number(nums: list) -> int:
    seen = set(nums)
    n = len(nums) + 1

    for num in range(n):
        if num not in seen:
            return num

    return seen


# Test Case
# 1
nums = [3, 0, 1]
result = missing_number(nums)
print(f'missing number is : {result}')

# 2
nums = [0, 1]
result = missing_number(nums)
print(f'missing number is : {result}')

# 3
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
result = missing_number(nums)
print(f'missing number is : {result}')
