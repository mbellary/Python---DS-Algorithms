from collections import deque

def canReach(arr: list[int], start: int) -> bool:

    def neighbours(index):
        indices = []
        right = index + arr[index]
        left = index - arr[index]
        if right <= len(arr) - 1:
            indices.append(right)
        if left >= 0:
            indices.append(left)
        return indices

    seen = set()
    queue = deque([start])

    while queue:
        step_idx = queue.popleft()

        if arr[step_idx] == 0:
            return True

        for neighbour in neighbours(step_idx):
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)

    return False

# Test Case
# 1
arr = [4,2,3,0,3,1,2]
start = 5
result = canReach(arr, start)
print(result)

# 2
arr = [3,0,2,1,2]
start = 2
result = canReach(arr, start)
print(result)