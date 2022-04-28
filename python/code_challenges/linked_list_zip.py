from data_structures.linked_list import LinkedList


def zip_lists(list_a, list_b):
    result = LinkedList()
    current_1 = list_a.head
    current_2 = list_b.head

    if current_1.next is None:
        current_1.next = current_2
    if current_2.next is None:
        current_2.next = current_1

    while current_1 and current_2:
        result.append(current_1)
        current_1 = current_1.next
        result.append(current_2)
        current_2 = current_2.next

    while current_1:
        result.append(current_1)
        current_1 = current_1.next

    while current_2:
        result.append(current_2)
        current_2 = current_2.next

    return result
