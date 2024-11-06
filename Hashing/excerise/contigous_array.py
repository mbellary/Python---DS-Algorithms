from collections import defaultdict
def contingous_array(nums: list) -> int:
    left = ans = 0
    counts = defaultdict(int)

    for right in range(len(nums)):
        counts[nums[right]] += 1

        while counts[0] > counts[1]:
            counts[nums[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

# Test Case
# 1
nums = [0, 1]
result = contingous_array(nums)
print(f'max length of the contiguous array is {result}')

# 2
nums = [0, 1, 0]
result = contingous_array(nums)
print(f'max length of the contiguous array is {result}')

# 3
nums = [0, 1, 0, 1]
result = contingous_array(nums)
print(f'max length of the contiguous array is {result}')

nums = [0,0,1,0,0,0,1,1]
result = contingous_array(nums)
print(f'max length of the contiguous array is {result}')