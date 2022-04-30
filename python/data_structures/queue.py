from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        if not self.front:
            self.front = Node(value)
            self.rear = self.front
            return

        temp = self.rear
        self.rear = Node(value)
        temp.next = self.rear
        return

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        old_front = self.front
        self.front = old_front.next
        old_front.next = None
        return old_front.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

