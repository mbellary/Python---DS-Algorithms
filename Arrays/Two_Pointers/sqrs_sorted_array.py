def sorted_squares(nums: list) -> list:

    nums_sqr = [num ** 2 for num in nums]
    ans = []

    while nums_sqr:
        val = min(nums_sqr)
        ans.append(val)
        nums_sqr.remove(val)
    return ans

# Test Case
# 1
nums_test = [-4, -1, 0, 3, 10]
result = sorted_squares(nums_test)
print(f'sorted squared array {result}')

#2
nums = [-7,-3,2,3,11]
result = sorted_squares(nums)
print(f'sorted squared array {result}')

# 2
nums = [-5,-3,-2,-1]
result = sorted_squares(nums)
print(f'sorted squared array {result}')