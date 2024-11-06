from collections import defaultdict

class Solution:

	def find_intersection_multiple_arrays(self, nums: list[list[int]]) -> list[int]:

		count = defaultdict(int)

		for arr in nums:
			for ele in arr:
				count[ele] += 1 # key will be created if not present.

		n = len(nums)
		ans = []

		for key in count:
			if count[key] == n:
				ans.append(key)

		return sorted(ans)