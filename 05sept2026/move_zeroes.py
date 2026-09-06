def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums

nums = [0, 1, 0, 3, 12]
print("Original array:", nums)
move_zeroes(nums)
print("After moving zeroes:", nums)
