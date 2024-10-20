def max_length_subarray_with_sum(nums, target):
    sum_map = {}  # Store cumulative sum and its corresponding index
    cumulative_sum = 0
    max_length = 0
    start_index = -1

    for i in range(len(nums)):
        cumulative_sum += nums[i] 
        
        if cumulative_sum == target:
            max_length = i + 1  
            start_index = 0
        
        if (cumulative_sum - target) in sum_map:

            length = i - sum_map[cumulative_sum - target]
            if length > max_length:
                max_length = length
                start_index = sum_map[cumulative_sum - target] + 1
        
        if cumulative_sum not in sum_map:
            sum_map[cumulative_sum] = i

    if max_length > 0:
        return nums[start_index:start_index + max_length]
    else:
        return []

nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8
result = max_length_subarray_with_sum(nums, target)
print("Longest subarray with sum {}: {}".format(target, result))