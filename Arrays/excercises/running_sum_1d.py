def running_sum(nums: list) -> list:
    curr = 0
    prefix_sum = [nums[0]]

    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    return prefix_sum


# Test Case
# 1
inp = [1, 2, 3, 4]
result = running_sum(inp)
print(f'The current running sum is {result}')

# 2
inp = [1, 1, 1, 1, 1]
result = running_sum(inp)
print(f'The current running sum is {result}')

# 3
inp = [3, 1, 2, 10, 1]
result = running_sum(inp)
print(f'The current running sum is {result}')
