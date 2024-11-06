def count_elements(nums: str) -> int:
    ans = 0
    seen = set(nums)

    for i in range(len(nums)):
        num = nums[i] + 1
        if num in seen:
            ans += 1

    return ans

# Test Case
# 1
arr = [1,2,3]
result = count_elements(arr)
print(f'Count of elements : {result}')


# 2
arr = [1,1,3,3,5,5,7,7]
result = count_elements(arr)
print(f'Count of elements : {result}')

