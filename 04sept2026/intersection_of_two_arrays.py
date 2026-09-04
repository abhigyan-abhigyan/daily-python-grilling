def intersection(nums1, nums2):
    set1 = set(nums1)
    result_set = set()
    for num in nums2:
        if num in set1:
            result_set.add(num)
    return list(result_set)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print("nums1:", nums1)
print("nums2:", nums2)
result = intersection(nums1, nums2)
print("Intersection:", result)
