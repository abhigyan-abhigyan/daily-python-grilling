def quickSort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    equal = []
    right = []

    for num in arr:

        if num < pivot:
            left.append(num)

        elif num == pivot:
            equal.append(num)

        else:
            right.append(num)

    return quickSort(left) + equal + quickSort(right)