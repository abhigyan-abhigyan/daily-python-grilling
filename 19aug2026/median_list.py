nums = [7, 2, 9, 4, 1]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

middle = len(nums) // 2

print(nums[middle])