def is_subsequence(seq: str, subseq: str) -> bool:
    i = j = 0
    while i < len(subseq) and j < len(seq):
        if subseq[i] == seq[j]:
            i += 1
        j += 1  # this will ensure that we don't end up in Infinite loop when subsequence is not found.

    return i == len(subseq)


# Test Cases
# 1 found subsequence
t = "ace"
s = "abcde"
result = is_subsequence(s, t)
if result:
    print(f' found "{t}" in {s}.')


# 2 No subsequence found
t = "eca"
s = "abcde"
result = is_subsequence(s, t)
if not result:
    print(f' not found "{t}" in {s}.')