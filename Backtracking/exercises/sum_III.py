

def combinationSum3(k: int, n: int) -> list[list[int]]:

    def bt(arr, j, curr):
        if len(arr) == k and sum(arr) == n:
            path.append(arr[:])
            return

        for i in range(j, 10):
            if curr + i <= n:
                arr.append(i)
                bt(arr, i + 1, curr + i)
                arr.pop()

    path = []
    bt([], 1,0)

    return path

# Test Case
# 1
k = 3
n = 7
result = combinationSum3(k, n)
print(f'{result}')

# 1
k = 3
n = 9
result = combinationSum3(k, n)
print(f'{result}')

k = 4
n = 1
result = combinationSum3(k, n)
print(f'{result}')