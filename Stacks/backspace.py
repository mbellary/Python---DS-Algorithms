def backspace(s: str, t: str) -> bool:
    def build(s):
        stack = []
        for char in s:
            if char != "#":
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)

    return build(s) == build(t)

#Test Case
# 1
s = "ab#c"
t = "ad#c"
result = backspace(s, t)
print(f'String comparision : {result}')