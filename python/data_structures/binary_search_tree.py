from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):

        def walk(root, new_node):

            if not root:
                return

            if new_node.value < root.value:
                # go left
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node
                # go right

        node_to_add = Node(value)

        if not self.root:
            self.root = node_to_add
            return

        walk(self.root, node_to_add)

    def contains(self, value):

        def walk(root, input_value):

            if root.value == input_value:  # found
                return True
            elif input_value > root.value and root.right is None:
                return False
            elif input_value < root.value and root.left is None:
                return False

            if root.value < input_value:
                return walk(root.right, input_value)

            elif root.value > input_value:

                return walk(root.left, input_value)

        return walk(self.root, value)
