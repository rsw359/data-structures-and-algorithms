
def quick_sort(arr, left, right):
    if left < right:
        position = partition(left, right, arr)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, right, position +1)

def partition(arr, left, right):
   pivot = arr[right]
   low = left - 1
   for i in range(left, right):
       if arr[i] <= pivot:
           low += 1
           swap(arr, i, low)

   swap(arr, right, low + 1)
   return low + 1

def swap(arr, i, low):
    temp = arr[i]
    arr[i]= arr[low]
    arr[low] = temp



