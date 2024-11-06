from collections import defaultdict

def connectedComponent(n: int, edges: list[list[int]]) -> int:
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(i):
        for neighbour in graph[i]:
            if neighbour not in seen:
                seen.add(neighbour)
                dfs(neighbour)

    seen = set()
    ans = 0

    for i in range(n):
        if i not in seen:
            ans += 1
            seen.add(i)
            dfs(i)
    return ans

# Test Case

n = 5
edges = [[0,1],[1,2],[3,4]]
result = connectedComponent(n, edges)
print(f'Total connected components are : {result}')

n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
result = connectedComponent(n, edges)
print(f'Total connected components are : {result}')