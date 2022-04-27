# Array-Binary-Search

The challenge here is to add a find the index of a value an array(or list in Python) without using any built in methods. The process needs to be explained to someone new to code.

## Approach & Efficiency

The approach taken here is to find the center of the array, then compare the input value to the midpoint value. Then we can shorten the number of values we need to search to find our desired index.

### Time Complexity

The Time Complexity for this algorithm  only grows one step when the amount of data elements doubles, making it: O(Log N)

![Code Challenge Whiteboard](array-binary-search.png)
