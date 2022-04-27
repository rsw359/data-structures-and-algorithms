
# Linked List Insertions

The challenge here is create three methods that modify a linked list. One to append the list, one to insert a node before one containing a specified value, and one to insert after a specified node.

## Approach & Efficiency

The approach taken here is to find node with the value we want, swap places between the next node and the specified node. The approach for the append method is to the end of the list, then append a new node to the end.

### Time Complexity

The Time Complexity for this algorithm grows along with the amount of data elements making it: O(N)

## Solution

To run this code, clone the repository, install pytest, and use the tests tests_linked_list_insertions.py

![Code Challenge Whiteboard](anotherWB.png)
