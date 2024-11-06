def numsSameConsecDiff(n: int, k: int) -> list[int]:
    d = 10
    def backtracking(i, arr):
        if len(arr) == n:
            path.append(int("".join([str(x) for x in arr])))
            return

        for digit in range(i, d):
            if not arr or abs(digit - arr[-1]) == k:
                arr.append(digit)
                backtracking(0, arr)
                arr.pop()

    path = []
    backtracking(1, [])

    return path

#Test Case
#1
n = 3
k = 7
result = numsSameConsecDiff(n, k)
print(f'{result}')

#1
n = 2
k = 1
result = numsSameConsecDiff(n, k)
print(f'{result}')
#
# #1
# n = 2
# k = 1
# result = numsSameConsecDiff(n, k)
# print(f'{result}')