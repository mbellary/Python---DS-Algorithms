def k_radius_avg(nums: list, k: int) -> list:
    n = len(nums)
    window = 2 * k
    avg = [-1] * n

    if k > n:
        return avg
    elif k == 0:
        avg = nums
        return avg

    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    for i in range(window, n):
        index = i - k
        avg[index] = (prefix[i] - prefix[i - window] + nums[i - window]) // (window + 1)

    return avg


# Test case
# 1
test_arr = [7, 4, 3, 9, 1, 8, 5, 2, 6]
test_k = 3
result = k_radius_avg(test_arr, test_k)
print(f'averages of subarray {result}')

# 2
test_arr = [100000]
test_k = 0
result = k_radius_avg(test_arr, test_k)
print(f'averages of subarray {result}')

# 3
test_arr = [8]
test_k = 100000
result = k_radius_avg(test_arr, test_k)
print(f'averages of subarray {result}')