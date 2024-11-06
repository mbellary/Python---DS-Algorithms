
class Solution:

	def find_unique_nums(self, nums:list) -> list:
		unique_nums = set(nums)
		result = []

		for num in unique_nums:
			if (num + 1 not in unique_nums) and (num - 1 not in unique_nums):
				result.append(num)

		return result