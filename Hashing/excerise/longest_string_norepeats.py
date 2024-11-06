from collections import defaultdict
def lengthOfLongestSubstring(s: str) -> int:
    left = ans = 0
    count = defaultdict(int)

    for right in range(len(s)):
        count[s[right]] += 1
        while max(count.values()) > 1:
            count[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

# Test Case
# 1
s = "abcabcbb"
result  = lengthOfLongestSubstring(s)
print(f'Length of the longest substring is {result}')

# 2
s = "bbbbb"
result = lengthOfLongestSubstring(s)
print(f'Length of the longest substring is {result}')

# 3
s = "pwwkew"
result = lengthOfLongestSubstring(s)
print(f'Length of the longest substring is {result}')