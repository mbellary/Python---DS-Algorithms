from collections import defaultdict

class Solution:

	def find_anagrams(self, s: list[str]) -> list[list[str]]:

		groups = defaultdict(list)

		for chars in s:
			key = "".join(sorted(chars))
			groups[key].append(chars)

		return groups.values()