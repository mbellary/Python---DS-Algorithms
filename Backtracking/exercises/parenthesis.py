def generateParenthesis(n: int) -> list[str]:

    parentheses = "".join(["()"] * n)
    print(parentheses)

    def bt(i, arr):
        if i == n * 2:
            ans.append("".join(arr))
            return

        for j in parentheses[i]:
            arr.append(j)
            bt(i + 1, arr)
            arr.pop()


    ans = []
    bt(0, [])
    return ans

# Test Case
#1
n = 3
result = generateParenthesis(n)
print(f'{result}')