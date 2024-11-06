from collections import defaultdict

def ransome_note(ransomNote: str, magazine: str) -> bool:

    ans = True
    count = defaultdict(int)
    for i in range(len(magazine)):
        count[magazine[i]] += 1

    for i in range(len(ransomNote)):
        if ransomNote[i] not in count:
            return False
        count[ransomNote[i]] -= 1
        if count[ransomNote[i]] == 0:
            del count[ransomNote[i]]

    return ans

# Test Case
# 1
ransomNote = "a"
magazine = "b"
result = ransome_note(ransomNote, magazine)
print(f'{result}')

# 2
ransomNote = "aa"
magazine = "ab"
result = ransome_note(ransomNote, magazine)
print(f'{result}')

# 3
ransomNote = "aa"
magazine = "aab"
result = ransome_note(ransomNote, magazine)
print(f'{result}')