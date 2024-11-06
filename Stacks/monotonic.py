
def monotonic_basics(nums):
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()

        stack.append(i)
    return stack

# Test Case
# 1
x = [40, 35, 32, 37]
res = monotonic_basics(x)
print(res)
