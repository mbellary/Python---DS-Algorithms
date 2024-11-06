def makeGood(s: str):
    stack = []

    for char in s:
        if not stack:
            stack.append(char)
        else:
            if (char == stack[-1].upper() or char.upper() == stack[-1]) and (char != stack[-1]):
                stack.pop()
            else:
                stack.append(char)
    return "".join(stack)

# Test Case
#1
s = "leEeetcode"
result = makeGood(s)
print(f"corrected string : {result}")

#2
s = "abBAcC"
result = makeGood(s)
print(f"corrected string : {result}")

#3
s = "s"
result = makeGood(s)
print(f"corrected string : {result}")

#4
s = "Pp"
result = makeGood(s)
print(f"corrected string : {result}")

#5
s = "kkdsFuqUfSDKK"
result = makeGood(s)
print(f"corrected string : {result}")