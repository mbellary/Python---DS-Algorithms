def removeDuplicates(s: str) -> str:
    stack = []

    for char in s:
        if not stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

    return "".join(stack)

#Test Case
#1
s = "abbaca"
result = removeDuplicates(s)
print(f"distinct string is {result}")
