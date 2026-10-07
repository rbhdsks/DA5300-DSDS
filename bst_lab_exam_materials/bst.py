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
            return Node(key)  # mistake fixed: naya node create karke return karo

        if key < node.key:
            node.left = self._insert(node.left, key)  # mistake fixed: node.left
        elif key > node.key:
            node.right = self._insert(node.right, key)  # mistake fixed: node.right

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return

        if key < node.key:
            node.left = self._delete(node.left, key)  # mistake fixed: node.left
        elif key > node.key:
            node.right = self._delete(node.right, key)  # mistake fixed: node.right
        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left
            else:
                succ = self._minimum_value_node(node.right)
                node.key = succ.key
                node.right = self._delete(node.right, succ.key)  # mistake fixed: update subtree, not key

        return node

    def _minimum_value_node(self, node):  # mistake fixed: correct parameters
        current = node

        while current.left is not None:
            current = current.left

        return current

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1

        left_node = self._height(node.left)
        right_node = self._height(node.right)

        return 1 + max(left_node, right_node)

    def number_of_nodes(self):
        return self._number_of_nodes(self.root)

    def _number_of_nodes(self, node):
        if node is None:
            return 0  # mistake fixed: empty subtree has zero nodes

        left_node = self._number_of_nodes(node.left)
        right_node = self._number_of_nodes(node.right)

        return 1 + left_node + right_node  # mistake fixed: count current node too

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


def process_file(filename):
    tree = BST()
    out = []

    with open(filename, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()

            if not line or line.startswith("#"):
                continue

            p = line.split()
            cmd = p[0].upper()

            if cmd == "I":
                tree.insert(int(p[1]))
            elif cmd == "D":
                tree.delete(int(p[1]))
            elif cmd == "H":
                out.append(str(tree.height()))
            elif cmd == "N":
                out.append(str(tree.number_of_nodes()))
            elif cmd == "IN":
                out.append(" ".join(map(str, tree.inorder())))
            elif cmd == "PRE":
                out.append(" ".join(map(str, tree.preorder())))
            elif cmd == "POST":
                out.append(" ".join(map(str, tree.postorder())))
            else:
                raise ValueError(f"Unknown command: {cmd}")

    return out


def main():
    if len(sys.argv) != 2:
        print("Usage: python bst.py test.txt")
        sys.exit(1)

    print("\n".join(process_file(sys.argv[1])))


if __name__ == "__main__":
    main()