
def maximum69Number (num: int) -> int:
    curr = num
    num_list = [n for n in str(num)]

    for i in range(len(num_list)):
        if num_list[i] == '6':
            num_list[i] = '9'
            val = int("".join(num_list))
            if val > curr:
                curr = val
            break

    return curr

# Test Case
# 1
num = 9669
result = maximum69Number(num)
print(f'max number is {result}')

# 2
num = 9996
result = maximum69Number(num)
print(f'max number is {result}')

#3
num = 9999
result = maximum69Number(num)
print(f'max number is {result}')