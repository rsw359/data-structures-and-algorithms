class LinkedList:
    """
    Put docstring here
    """

    # initialize the class
    def __init__(self):
        self.head = None

    def __str__(self):
        # Take in a response and return a string of the current nodes while traversing the list
        input_response = ""
        current = self.head
        while current:
            input_response += f"{{ {current.value} }} -> "
            current = current.next
        return input_response + "NULL"

    # create new nodes and reassign the head
    def insert(self, value):
        old_head = self.head
        self.head = Node(value, self.head)
        self.head.next = old_head

    # check to see if the value exists
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
