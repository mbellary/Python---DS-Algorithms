def answerQueries(nums: list[int], queries: list[int]) -> list[int]:
    def binarySearch(nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return len(nums[:mid + 1])

            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    answers = []
    nums.sort()
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for i in range(len(queries)):
        index = binarySearch(prefix_sum, queries[i])
        answers.append(index)
    return answers

# Test Case
# 1
nums = [4, 5, 2, 1]
queries = [3, 10, 21]
result = answerQueries(nums, queries)
print(f'{result}')

# 2
nums = [2,3,4,5]
queries = [1]
result = answerQueries(nums, queries)
print(f'{result}')
# 3
# nums = [4, 5, 2, 1]
# queries = [3, 10, 21]
# result = answerQueries(nums, queries)