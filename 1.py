def merge_sort(list1):
    if len(list1) <= 1:
        return list1

    middle = len(list1) // 2

    left = merge_sort(list1[:middle])
    right = merge_sort(list1[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result
