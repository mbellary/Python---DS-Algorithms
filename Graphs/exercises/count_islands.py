from collections import defaultdict


def maxAreaOfIsland(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    def isValid(row, col):
        return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

    def dfs(row, col):
        ans = 0
        for dx, dy in directions:
            next_row, next_col = row + dy, col + dx
            if isValid(next_row, next_col) and (next_row, next_col) not in seen:
                ans += 1
                seen.add((next_row, next_col))
                ans += dfs(next_row, next_col)
        return ans

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seen = set()
    max_area = 0
    for row in range(m):
        for col in range(n):
            if (row, col) not in seen and grid[row][col] == 1:
                seen.add((row, col))
                curr_area = dfs(row, col)
                curr_area += 1
                if curr_area >= max_area:
                    max_area = curr_area
    return max_area


# Test Case
# 1
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

result = maxAreaOfIsland(grid)
print(f'Max area of island : {result}')

# 2
grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
result = maxAreaOfIsland(grid)
print(f'Max area of island : {result}')

grid = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
result = maxAreaOfIsland(grid)
print(f'Max area of island : {result}')

grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
result = maxAreaOfIsland(grid)
print(f'Max area of island : {result}')
