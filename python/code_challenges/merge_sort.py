def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2  # find the midpoint

        left = list[:mid]  # split left
        right = list[mid:]  # split right

        # recursive call
        merge_sort(left)
        merge_sort(right)

        i = 0  # left index
        j = 0  # right index

        k = 0  # merged list index

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i = i + 1
            else:
                list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list


