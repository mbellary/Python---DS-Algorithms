from collections import defaultdict

class Solution:
	
	def find_longest_substring(self, s: str, k: int) -> int:

		count = defaultdict() 
		left = 0
		ans = 0

		for right in range(len(s)):
			rightkey = s[right]
			count[rightkey] = 1

			while len(count) > k:
				leftkey = s[left]
				count[leftkey] -= 1

				if count[leftkey] == 0:
					del count[leftkey]
				left = left + 1

			ans = max(ans, right - left + 1)
		return ans


