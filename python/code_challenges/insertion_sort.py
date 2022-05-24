

def insertion_sort(arr):
    for index in range(1, len(arr)):
        prev_index = index-1
        temp = arr[index]

        while prev_index>=0 and temp < arr[prev_index]:
            arr[prev_index + 1] = arr[prev_index]
            prev_index = prev_index - 1

        arr[prev_index + 1]  = temp

    return arr
