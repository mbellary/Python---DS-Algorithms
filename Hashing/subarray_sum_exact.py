from collections import defaultdict

class Solution:

	def find_subarray_k_exact(self, nums: list[int], k: int) -> int:

		count = defaultdict(int)  # int is important for autoinitialization.
		count[0] = 1
		curr = 0
		ans = 0

		for num in nums:
			curr += num
			count[curr] +=  1
			ans += count[curr - k]

		return ans

