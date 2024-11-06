from collections import deque


def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    m = len(maze)
    n = len(maze[0])

    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

    def is_exit(row, col):
        if (row, col) == (entrance[0], entrance[1]):
            return False
        if (row == 0 or row == m - 1) and maze[row][col] == ".":
            return True
        elif (col == 0 or col == n - 1) and maze[row][col] == ".":
            return True
        else:
            return False

    queue = deque([(entrance[0], entrance[1], 0)])
    seen = {(entrance[0], entrance[1])}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        row, col, steps = queue.popleft()

        if is_exit(row, col):
            return steps

        for dx, dy in directions:
            next_row, next_col = row + dy, col + dx
            if is_valid(next_row, next_col):
                if (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

    return -1

# Test Case
#1
maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
result = nearestExit(maze, entrance)
print(f'The nearest exit is {result} step away.')

# 2

maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1, 0]
result = nearestExit(maze, entrance)
print(f'The nearest exit is {result} step away.')

# 3
maze = [[".","+"]]
entrance = [0, 0]
result = nearestExit(maze, entrance)
print(f'The nearest exit is {result} step away.')

#4
maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
entrance = [0,1]
result = nearestExit(maze, entrance)
assert(result == 12)
print(f'The nearest exit is {result} step away.')

