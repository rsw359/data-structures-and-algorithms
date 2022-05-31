from data_structures.linked_list import LinkedList


class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self.pockets = [None] * self.size

    def hash(self, key):
        sum_chars = 0
        for char in key:
            sum_chars += ord(char)

        primed = sum_chars * 599

        index = primed % self.size
        return index

    def set(self, key, value):
        idx = self.hash(key)

        pocket = self.pockets[idx]

        if pocket is None:
            pocket = LinkedList()
            self.pockets[idx] = pocket

        pocket.insert((key, value))

    def get(self, key):
        idx = self.hash(key)
        pocket = self.pockets[idx]

        current = pocket.head

        while current:
            pair = current.value
            current_key = current.value[0]
            if current_key == key:
                return pair[1]

            current = current.next

        return None

    def keys(self):
        all_keys = []
        for pocket in self.pockets:
            if pocket is not None:
                current = pocket.head
                while current:
                    pair = current.value
                    current_key = pair[0]
                    all_keys.append(current_key)
                    current= current.next
        return all_keys

