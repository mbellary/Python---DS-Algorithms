from collections import defaultdict

def max_balloons(text: str) -> int:
    instances = 0
    match = 'balloon'
    count = defaultdict(int)

    for i in range(len(text)):
        if text[i] in match:
            count[text[i]] += 1


    while len(count):
        for i in range(len(match)):
            if match[i] not in count:
                return instances
            count[match[i]] -= 1
            if count[match[i]] == 0:
                del count[match[i]]
        instances += 1

    return instances


# Test Case
text = "nlaebolko"
result = max_balloons(text)
print(f'Total instances : {result}')

# 2
text = "loonbalxballpoon"
result = max_balloons(text)
print(f'Total instances : {result}')

# 3
text = "leetcode"
result = max_balloons(text)
print(f'Total instances : {result}')
