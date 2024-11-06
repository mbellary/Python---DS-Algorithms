
class Solution:

	def repeatedChars(self, s: str) -> str:
		key_set = set()
		for c in s:
			if c in key_set:
				return c
			key_set.add(c)

		return "no duplicate char found!"