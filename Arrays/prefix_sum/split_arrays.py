class Solution:

	def find_valid_split_arrays(self, nums: list[int]) -> int:

		prefix = [nums[0]]
		for i in range(1, len(nums)):
			prefix.append(nums[i] + prefix[-1])

		ans = 0
		for i in range(len(nums) - 1): # -1 to avoid splitting on last element
			left_section = prefix[i]
			right_section = prefix[-1] - prefix[i]  # prefix sum : (p[j] - p[i - 1]) or (p[j] - p[i] + nums[i]) (to handle out of bound index 0)

			if left_section >= right_section:
				ans += 1
		return ans

	# prefix sum without using arrays
	def split_without_array(self, nums: list[int]) -> int:

		total = sum(nums)
		left_section = 0
		ans = 0

		for i in range(len(nums) - 1):
			left_section += nums[i]
			right_section = total - left_section

			if left_section >= right_section:
				ans += 1
		return ans
