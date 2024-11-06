def validParentheses(s: str) -> bool :
    stack = []
    matchings = {"(": ")", "[": "]", "{": "}"}

    for c in s:
        if c in matchings:
            stack.append(c)
        else:
            if not stack: # empty stack
                return False
            last_opening = stack.pop()
            if matchings[last_opening] != c:
                return False

    return not stack



# Test Case
#1
s1 = "{([]){}}"
result = validParentheses(s1)
print(f'string is {result}')
