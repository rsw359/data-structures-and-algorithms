class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        # Take in a response and return a string of the current nodes while traversing
        response = ""
        current = self.head
        while current:
            response += f"{{ {current.value} }} -> "
            current = current.next
        return response + "NULL"

    def insert(self, value):
        old_head = self.head
        self.head = Node(value, self.head)
        self.head.next = old_head

    def includes(self, value):
        # self.value = value
        current = self.head

        while current:
            if current.value == value:
                return True

            current = current.next

        return False


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError:
    pass
