from data_structures.queue import Queue
from data_structures.stack import Stack


def multi_bracket_validation(string):
    set_dictionary = {'}': "{", ')': '(', ']': '['}  # dictionary of  closers and their pairs
    open_bracs = {'{', '(', '['}  # set of openers
    stack = Stack()

    for char in string:  # iterate through the string
        if char in open_bracs:  # check if it is an open brac
            stack.push(char)  # if it is, push it to the stack
        elif char in set_dictionary:  # if it isnt, compare it to the key value pair
            if stack.is_empty() or stack.pop() != set_dictionary[char]:
                return False  # if nothing has been passed into the stack, or the prev char doesn't match the closer
    return stack.is_empty()  # if the string is true, all chars will have been popped from the stack


