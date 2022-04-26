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

    def append(self, new_value):
        new_node = Node(new_value)
        # if self.head is None:
        #     self.head = new_node
        #     return
        # else:
        saved_value = self.head
        while saved_value.next is not None:
            saved_value = saved_value.next
        saved_value.next = new_node

    def insert_before(self, value, new_value):
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError

        new_node = Node(new_value)
        current = self.head
        if current.value is value:
            new_node.next = self.head
            self.head = new_node

        while current.next is not None:
            if current.next.value is value:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

    def insert_after(self, value, new_value):
        current = self.head
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError

        while current.next is not None:
            if current.value is value:
                current.next = Node(new_value, current.next)
                break
            else:
                current = current.next


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError(Exception):
    pass
