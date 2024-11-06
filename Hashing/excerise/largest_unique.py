from collections import defaultdict

def largestUniqueNumber(nums: list[int]) -> int:

    count = defaultdict(int)
    max = -1

    for num in nums:
        count[num] += 1

    for k, v in count.items():
        if k > max and v == 1:
            max = k
    return max

# Test Case
#1
nums = [5,7,3,9,4,9,8,3,1]
result = largestUniqueNumber(nums)
print(f'{result}')

#2
nums = [9,9,8,8]
result = largestUniqueNumber(nums)
print(f'{result}')