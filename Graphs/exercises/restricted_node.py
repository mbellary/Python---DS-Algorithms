from collections import defaultdict


def reachableNodes(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    #print(graph)
    if not (len(graph)) or n == 2:
        return 1

    def dfs(node):
        ans = 0
        for neighbour in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                ans += 1
                ans += dfs(neighbour)
        return ans

    seen = set(restricted)
    seen.add(0)

    return dfs(0) + 1


# Test Cases
# 1
n = 7
edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
restricted = [4, 5]
result = reachableNodes(n, edges, restricted)
print(f'reachable nodes are : {result}')

# 2
n = 7
edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
restricted = [4, 2, 1]
result = reachableNodes(n, edges, restricted)
print(f'reachable nodes are : {result}')
#
n = 4
edges = [[2, 1], [1, 0], [0, 3]]
restricted = [3, 2]
result = reachableNodes(n, edges, restricted)
print(f'reachable nodes are : {result}')

n = 7
edges = [[0, 3], [2, 0], [4, 2], [4, 1], [0, 6], [5, 1]]
restricted = [6, 3, 4, 2, 5]
result = reachableNodes(n, edges, restricted)
print(f'reachable nodes are : {result}')

n = 10
edges = [[8, 2], [2, 5], [5, 0], [2, 7], [1, 7], [3, 8], [0, 4], [3, 9], [1, 6]]
restricted = [9, 8, 4, 5, 3, 1]
result = reachableNodes(n, edges, restricted)
print(f'reachable nodes are : {result}')
