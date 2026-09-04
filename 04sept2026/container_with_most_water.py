def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        current_area = width * h
        max_water = max(max_water, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Heights array:", heights)
result = max_area(heights)
print("Maximum water area:", result)
