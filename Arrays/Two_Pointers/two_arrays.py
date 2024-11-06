def combine(arr1: list, arr2: list) -> list:
    i = j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


# Test Cases
# 1 arrays are positive integers

nums1 = [1, 4, 7, 20]
nums2 = [3, 5, 6]
result = combine(nums1, nums2)
print(f'Sorted Array with positive integers {result}')

# 2  arrays are negative integers - Inputs MUST be sorted
nums1 = [-20, -7, -4, -1]
nums2 = [-6, -5, -3]
result = combine(nums1, nums2)
print(f'Sorted Array with negative integers {result}')
