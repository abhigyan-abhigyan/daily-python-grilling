def is_monotonic(nums):
    increasing = True
    decreasing = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            increasing = False
        if nums[i] < nums[i + 1]:
            decreasing = False
    return increasing or decreasing

test1 = [1, 2, 2, 3]
print(f"Is {test1} monotonic?:", is_monotonic(test1))

test2 = [1, 3, 2]
print(f"Is {test2} monotonic?:", is_monotonic(test2))
