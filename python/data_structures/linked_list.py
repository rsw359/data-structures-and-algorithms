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
        ### intantiate a new node
        ### set the head

        new_node = Node(new_value)

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

    def kth_from_end(self, k):

        l_length = 0  # length of ll
        current = self.head  # set the head

        while current:
            current = current.next  # traversal
            l_length = l_length + 1  # calc the length so we can subtract k

        if k >= l_length:  # If k is greater than the length of ll > raise the error
            raise TargetError

        if k < 0:  # If k is negative number > raise the target error
            raise TargetError

        if l_length >= k:
            current = self.head
            for i in range(l_length - k - 1):  # we have to subtract on because the 0 is counted in the length
                current = current.next

        return current.value


def zip_lists(list_a, list_b):
    # current_1 = list_a.head
    # current_2 = list_b.head
    # temp_1 = current_1.next
    # temp_2 = current_2.next

    # while current_1 is not None:
    #     current_1.next = current_2
    #     current_2.next = temp_1
    #     temp_1.next = current_1
    #     temp_2.next = current_2
    #
    #     if current_1.next is None:
    #         current_1.next = current_2
    #     if current_2.next is None:
    #         current_2.next = current_1

    return list_a


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError(Exception):
    pass
