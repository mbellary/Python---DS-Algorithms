def is_pangram(s: str) -> bool:
    alphabets = 26
    seen = set()
    for c in s:
        seen.add(c)

    return len(seen) == alphabets


# Test Case
# 1
sentence = "thequickbrownfoxjumpsoverthelazydog"
result = is_pangram(sentence)
print(f'is pangram {result}')

# 2
sentence = "leetcode"
result = is_pangram(sentence)
print(f'is pangram {result}')