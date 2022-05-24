# Insertion-sort

## In this exercise we are implementing a function that can sort an array in ascending order.

```
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

### In the first pass through:

We evaluate whether the value of index 1(**temp = array[ i ]**) is less than value of index 0(**j = i - 1**). The value of temp is set to index one’s value.

If temp is less than **j**, we replace the value of **i** with the value of j.

Since that is not the case, we do nothing and return to the top of the loop

### On the second pass:

- i is set to 2 since we are on the second iteration of the loop.
- j is set to 1(**j = i - 1)**
- temp is set to the value of index 2, which is 1

In our loop:

- We evaluate whether the value of temp is less than the value of index j: 1 < 3
- Since that is true, we set 3 to the position of j+1, or the second index of our array.
  - [2, 3, 3,4]

We then set j to j-1, which the 0 index of our array and enter our while loop again.

Next we check if the value of temp is less than the value of j, or the zero index at this point, which it is: 1 < 2

We then set the value of index 1 to the value of current value of j:

- [2, 2, 3,4]

We then set j to j-1 which is -1, and enter out loop again.

Since j is less than 0, we break out of the loop.

Finally, we set the zero index (array[j + 1]) to temp, which is still 10.

### Begin pass 3!

- i is set to 3 since we are on the second iteration of the loop.
- j is set to 2(**j = i - 1)**
- temp is set to the value of index 3, which is 4

This go around, **temp** is not less than the value of **j**, so we don’t enter the loop.

Finally, we set the value of index 3 (array[j + 1]) to temp(4), and we’ve reached the end of the array.

![IMG_0363.PNG](IMG_0363.PNG)

The time complexity for Insertion-Sort is O(n^2) because the algorithm has to iterate through the array and do the same number of steps for each index.

The space is O(1) since the size of the data does not change throughout the process.
