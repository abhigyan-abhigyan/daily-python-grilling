def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1
    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1
    return result

nums = [-4, -1, 0, 3, 10]
print("Original array:", nums)
res = sorted_squares(nums)
print("Sorted squares:", res)
