

from collections import deque
def minMutation(startGene: str, endGene: str, bank: list[str]) -> int:
    char2int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    int2char = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    def gene_str(gene):
        chars = [*gene]
        mapped = [str(char2int[c]) for c in chars]
        return "".join(mapped)

    def reversed(genes):
        reversed = []
        for gene in genes:
            chars = [*gene]
            mapped = [(int2char[int(c)]) for c in chars if int(c) in int2char]
            reversed.append("".join(mapped))
        return reversed

    def neighbors(node):
        ans = []
        node = gene_str(node)
        for i in range(8):
            num = int(node[i])
            for change in [-1, 2, 3, 1]:
                x = (num + change) % 4
                ans.append(node[:i] + str(x) + node[i + 1:])
        mapped = reversed(ans)
        #print(mapped)
        return mapped

    seen = set()
    queue = deque([(startGene, 0)])
    while queue:
        gene, steps = queue.popleft()
        if gene == endGene:
            return steps

        for neighbor in neighbors(gene):
            if neighbor not in seen and neighbor in bank:
                seen.add(neighbor)
                queue.append((neighbor, steps + 1))

    return -1

#Test Case
#1
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
result = minMutation(startGene, endGene, bank)
print(result)
#
#2
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
result = minMutation(startGene, endGene, bank)
print(result)
#
#2
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = []
result = minMutation(startGene, endGene, bank)
print(result)

#2
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
result = minMutation(startGene, endGene, bank)
print(result)
