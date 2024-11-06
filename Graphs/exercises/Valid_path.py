from collections import defaultdict

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    if not edges and n != 0 and source == destination:
        return True

    if source == destination:
        return True

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(source):
        valid_path = 0
        for neighbour in graph[source]:
            if neighbour not in seen:
                if neighbour == destination:
                    valid_path = 1
                seen.add(neighbour)
                valid_path += dfs(neighbour)
        return bool(valid_path)

    seen = set()
    for i in range(n):
        if i not in seen and i == source:
            seen.add(i)
            return dfs(i)

# Test Case
#1
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
result = validPath(n, edges, source, destination)
print(f'valid path {result}')

#1
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
result = validPath(n, edges, source, destination)
print(f'valid path {result}')

n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source = 5
destination = 9
result = validPath(n, edges, source, destination)
print(f'valid path {result}')

n = 10
edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source = 7
destination = 5
result = validPath(n, edges, source, destination)
print(f'valid path {result}')

