from data_structures.stack import Stack



class PseudoQueue:

    def __init__(self):
        self.inn = Stack()
        self.out = Stack()

    def enqueue(self, value):
        self.inn.push(value)

    def dequeue(self):

        while self.inn.top:
            inn_item = self.inn.pop()
            self.out.push(inn_item)

        if self.out.top:
            return_node = self.out.pop()
        while self.out.top:
            out_item = self.out.pop()
            self.inn.push(out_item)
        return return_node


