def letterCombinations(digits: str) -> list[str]:
    digit_char = {
        1: "",
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }
    char_digit = {
        "" : 1,
        "a" : 2,
        "b" : 2,
        "c" : 2,
        "d" : 3,
        "e" : 3,
        "f" : 3,
        "g" : 4,
        "h" : 4,
        "i" : 4,
        "j" : 5,
        "k" : 5,
        "l" : 5,
        "m" : 6,
        "n" : 6,
        "o" : 6,
        "p" : 7,
        "q" : 7,
        "r" : 7,
        "s" : 7,
        "t" : 8,
        "u" : 8,
        "v" : 8,
        "w" : 9,
        "x" : 9,
        "y" : 9,
        "z" : 9
    }

    num_digits = [*digits]
    k = len(num_digits)
    m = len(set(num_digits))
    chars = []
    target = 0
    for digit in num_digits:
        target += int(digit)
    if digits == "":
        return []

    if len(num_digits) == 1:
        return digit_char[int(num_digits[0])]

    for i in range(len(num_digits)):
        chars += digit_char[int(num_digits[i])]

    def backtrace(path, p, nums):

        if len(path) == k and sum(nums) == target and len(set(nums)) == m:
            ans.append("".join(path))
            return

        for j in range(p, len(chars)):
            path.append(chars[j])
            nums.append(char_digit[chars[j]])
            backtrace(path, j + 1, nums)
            path.pop()
            nums.pop()

    ans = []
    backtrace([], 0, [])
    return list(set(ans))


# Test Case
# 1
digits = "23"
result = letterCombinations(digits)
print(f'{result}')

#2
digits = ""
result = letterCombinations(digits)
print(f'{result}')

#3
digits = "2"
result = letterCombinations(digits)
print(f'{result}')

#3
digits = "22"
result = letterCombinations(digits)
print(f'{result}')