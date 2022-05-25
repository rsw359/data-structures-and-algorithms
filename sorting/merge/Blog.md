# Merge Sort

Let’s take a look at  another sorting algorithm.

Merge Sort breaks a list into its smallest parts using recursion, and  then merges the parts back together in ascending order. This is one of the most efficient ways to sort a list or array!

Let’s step through this pseudo code:

```

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

It’s a bit long, but let’s take it one step at a time.

Let’s use this sample list:  [ 5 ,6 ,7 ,4 ]

n is defined as the length of the array.

In the next three lines, we split the list into pieces by declaring the midpoint, left and right parts of the list.

- midpoint split looks like this: [ 5, 6 ] [ 7, 4]
- left split [ 5, 6 ]
- right split [ 7, 4  ]

Then the recursion comes in when we call the function again and split the left and right parts until they are composed of only one value each.

- left splits again: [5] and [6]
- right splits again,  too: [7] [4]

Our first ***if*** conditional says that we keep splitting as long as the length of our lists are greater than one. But we now have 4 lists that contain one value each. Time to sort then merge them.

We need to use a variable for each of the values ad set them to zero. After that, we can compare them and order them .

**i** is the left index, **j** is the right index, and **k** is the merged list’s index.

Our while loop says that as long as these indices are less than the length of their respective sides (**i** for left and **j** for the right), we can compare them.

If the value of the left index is less than the right side value, we put it in the merged list. Otherwise the right side value gets put in the merged list.

Like this:

[5] [6]   |   [4] [7]

[5,6]  [4,7]

Now, we compare the values at each index:

For the zero index, we compare 5 and 4. 4 is the smaller number, so it gets tossed into the list

- Merged [4]

Next we compare 5 and 7. 5 goes in!

- Merged [4, 5]

Now compare 6 and seven. You guessed it! 6 jumps into the pool.

- Merged [4, 5, 6]

7 is all that’s left. Get in there, 7!

- Merged [4, 5, 6, 7]

We’ve sorted our list, and the last thing to do now is to ***return*** the list.
