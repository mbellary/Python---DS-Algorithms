from collections import defaultdict

def numJewelsInStones(jewels: str, stones: str) -> int:

    ans = 0
    count = defaultdict(int)
    for char in range(len(stones)):
        if stones[char] in jewels:
            count[stones[char]] += 1

    ans = sum(count.values())

    return ans

# Test Case
#1
jewels = "aA"
stones = "aAAbbbb"
result = numJewelsInStones(jewels, stones)
print(f'{result} stones are also jewels')

#2
jewels = "z"
stones = "ZZ"
result = numJewelsInStones(jewels, stones)
print(f'{result} stones are also jewels')