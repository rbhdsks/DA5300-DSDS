import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return  # mistake: yahan return Node(key) hona chahiye

        if key < node.key:
            self.left = self._insert(node.left, key)  # mistake: self.left nahi, node.left
        elif key > node.key:
            self.right = self._insert(node.right, key)  # mistake: self.right nahi, node.right

        return node
        # TODO: implement insertion
        # pass

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return

        if key < node.key:
            self.left = self._delete(node.left, key)  # mistake: self.left nahi, node.left
        elif key > node.key:
            self.right = self._delete(node.right, key)  # mistake: self.right nahi, node.right
        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left
            else:
                succ = self._minimum_value_node(node.right)
                node.key = succ.key
                node.key = self._delete(node.right, succ.key)  # mistake: node.right update karna hai

        return node

    def _minimum_value_node(node, key):  # mistake: parameters (self, node) hone chahiye
        current = node
        while current.left is not None:
            current = current.left
        return current

        # TODO: implement deletion
        # pass

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1

        left_node = self._height(node.left)
        right_node = self._height(node.right)
        return 1 + max(left_node, right_node)

        # TODO: implement height
        # Height is measured in edges. Empty tree = -1.
        # pass

    def number_of_nodes(self):
        return self._number_of_nodes(self.root)

    def _number_of_nodes(self, node):
        if node is None:
            return  # mistake: empty subtree ka count 0 hai, None nahi

        left_node = self._number_of_nodes(node.left)
        right_node = self._number_of_nodes(node.right)
        return left_node + right_node  # mistake: current node ke liye +1 missing hai

        # TODO: implement number of nodes
        # pass

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return

        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)

        # TODO: implement inorder traversal
        # pass

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is None:
            return

        result.append(node.key)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

        # TODO: implement preorder traversal
        # pass

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is None:
            return

        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.key)

        # TODO: implement postorder traversal
        # pass