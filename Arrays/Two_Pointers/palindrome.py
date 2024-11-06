def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


# Test Cases
# 1 is a palindrome
s = "abcdcba"
result = is_palindrome(s)

if result:
    print(f'#1 => string is a palindrome.')

# 2 not a palindrome
s = "aceba"
result = is_palindrome(s)

if not result:
    print(f'#2 => string is a not a palindrome.')
