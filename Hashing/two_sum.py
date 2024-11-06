

def find_sum_indices(nums, target):

	elem_map = {}

	for i in range(len(nums)):
		val1 = target - nums[i]

		if val1 in elem_map:
			return [i, elem_map[val1]]

		elem_map[nums[i]] = i
