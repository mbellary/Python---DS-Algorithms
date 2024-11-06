from collections import defaultdict

def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph)
    edges = defaultdict(list)

    for i in range(len(graph)):
        edges[i] = graph[i]
    def bt(curr, i):

        if curr[0] == 0 and curr[-1] == n - 1:
            ans.append(curr[:])
            return

        for j in range(i, len(curr)):
            for neighbour in edges[curr[j]]:
                if neighbour not in curr:
                    curr.append(neighbour)
                    bt(curr, j + 1)
                    curr.pop()

    ans = []
    bt([0], 0)
    return ans

# Test Case
#1
graph = [[1,2],[3],[3],[]]
result = allPathsSourceTarget(graph)
print(f'{result}')

# 2
graph = [[4,3,1],[3,2,4],[3],[4],[]]
result = allPathsSourceTarget(graph)
print(f'{result}')
