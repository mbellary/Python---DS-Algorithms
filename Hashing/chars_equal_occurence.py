from collections import defaultdict, Counter

class Solution:

	def is_equal_occurence(self, s: str) -> bool:
		
		count = defaultdict(int)
		for char in s:
			count[char] += 1
		frequency = count.values()

		return len(set(frequency)) == 1

	def built_in_counter(self, s: str) -> bool:
		return len(set(Counter(s).values())) == 1