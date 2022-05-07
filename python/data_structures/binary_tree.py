class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):

        def walk(root, values):
            if not root:
                return

            values.append(root.value)

            walk(root.left, values)

            walk(root.right, values)

        ordered_vals = []

        walk(self.root, ordered_vals)

        return ordered_vals

    def in_order(self):

        def walk(root, values):
            if not root:
                return

            walk(root.left, values)

            values.append(root.value)

            walk(root.right, values)

        ordered_vals = []

        walk(self.root, ordered_vals)

        return ordered_vals

    def post_order(self):
        def walk(root, values):
            if not root:
                return

            walk(root.left, values)

            walk(root.right, values)

            values.append(root.value)

        ordered_vals = []

        walk(self.root, ordered_vals)

        return ordered_vals


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
