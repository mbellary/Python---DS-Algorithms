import os
def simplifyPath(path: str) -> str:
    stack = []
    tokens = path.split('/')
    tokens2 = []
    for token in tokens:
        if token == "":
            tokens2.append('/')
        else:
            tokens2.append(token)
            tokens2.append('/')

    if not stack:
        stack.append(tokens2.pop())

    return "".join(stack)



# Test Case
#1
path = "/home/"
result = simplifyPath(path)
print(f'simplied canonical path is : {result}')
#
# 2
path = "/home//foo/"
result = simplifyPath(path)
print(f'simplied canonical path is : {result}')
#
# 3
path = "/home/user/Documents/../Pictures"
result = simplifyPath(path)
print(f'simplied canonical path is : {result}')
#
# 4
path = "/../"
result = simplifyPath(path)
print(f'simplied canonical path is : {result}')

5
path = "/.../a/../b/c/../d/./"
result = simplifyPath(path)
print(f'simplied canonical path is : {result}')

# #6
path = "/a/./b/../../c/"
result = simplifyPath(path)
print(f'simplied canonical path is : {result}')