def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Pair indices:", result)
print("Values:", nums[result[0]], "+", nums[result[1]], "=", target)
