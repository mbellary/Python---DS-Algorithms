class Solution:

	def find_subarray_sum(self, nums: list[int], q: list[list[int]], limit:int) -> list[bool]:

		prefix = [nums[0]]
		for i in range(1, len(nums)):
			prefix.append(nums[i] + prefix[- 1])

		ans = []
		for j in q:
			sum_subarray = prefix[j[0]] + prefix[j[1]]
			if sum_subarray <= limit:
				ans.append("True")
			else:
				ans.append("False")

		return ans

	def answer_queries(self, nums: list[int], q: list[list[int]], limit:int) -> list[bool]:

		prefix = [nums[0]]
		for i in range(1, len(nums)):
			prefix.append(nums[i] + prefix[-1])

		ans = []
		for x, y in q:
			curr = prefix[y] - prefix[x] + nums[x]
			ans.append(curr < limit)

		return ans