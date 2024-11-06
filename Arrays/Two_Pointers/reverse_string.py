def reverse_string(s: list) -> list:
    left = 0
    right = len(s) - 1

    while left < right:
        s_l = s[left]
        s_r = s[right]
        s[left] = s_r
        s[right] = s_l
        left += 1
        right -= 1

    return s


# Test Case
# 1
s = ["h", "e", "l", "l", "o"]
output = ["o", "l", "l", "e", "h"]
result = reverse_string(s)

if result == output:
    print(f'Successfully reversed string! : {result}')
else:
    print(f'String reversal unsuccessful for test case 1!')

# 2
output = ["h", "a", "n", "n", "a", "H"]
s = ["H", "a", "n", "n", "a", "h"]
result = reverse_string(s)

if result == output:
    print(f'Successfully reversed string! : {result}')
else:
    print(f'String reversal unsuccessful for test case 2!')


# Solution:1 - Two Pointer
def reverse_string_solution(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1


# Test Case
# 1
s = ["h", "e", "l", "l", "o"]
output = ["o", "l", "l", "e", "h"]
reverse_string_solution(s)

print(f'[SOLUTION] Successfully reversed string! : {s}')
