def find_length_string(s: str, k: int) -> int:
    left = curr = ans = 0

    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > k:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


# Test Case
# 1
s = "1101100111"
k = 1
result = find_length_string(s, k)
print(f'Length of the longest subarray string {result}')