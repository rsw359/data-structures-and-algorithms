from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    breadth_queue = Queue()
    breadth_queue.enqueue(tree.root)
    output = []

    if tree is None:
        return output
    if tree.root is None:
        return output

    while not breadth_queue.is_empty():
        front = breadth_queue.dequeue()
        output.append(front.value)
        if front.left:
            breadth_queue.enqueue(front.left)

        if front.right:
            breadth_queue.enqueue(front.right)

    return output
