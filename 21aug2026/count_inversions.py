def merge_count(left, right):

    result = []
    count = 0

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])

            # Every remaining element in left
            # forms an inversion with right[j]
            count += len(left) - i

            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, count


def merge_sort_count(arr):

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, left_count = merge_sort_count(arr[:mid])
    right, right_count = merge_sort_count(arr[mid:])

    merged, merge_count = merge_count(left, right)

    total_count = left_count + right_count + merge_count

    return merged, total_count


arr = [2, 4, 1, 3, 5]

sorted_arr, count = merge_sort_count(arr)

print("Sorted:", sorted_arr)
print("Inversions:", count)