import sys

class Node:

    def __init__(self, val = None):
        if val is None:
            self.val = None
            self.left = None
            self.right = None
        else:
            self.val = val
            self.left = Node(None)
            self.right = Node(None)

    def is_empty(self):
        return self.val is None
    
    def is_leaf(self):
        return not self.is_empty() and self.left.is_empty() and self.right.is_empty()
    
    def insert(self, v):
        if self.is_empty():
            self.val = v
            self.left = Node(None)
            self.right = Node(None)
            return
        
        if self.val == v:
            return
        
        if v < self.val:
            self.left.insert(v)
        else:
            self.right.insert(v)
    
    def delete(self, v):
        if self.is_empty():
            return
        
        if v < self.val:
            self.left.delete(v)
        elif v > self.val:
            self.right.delete(v)
        else:
            if self.is_leaf():
                self.make_empty()
            elif self.left.is_empty():
                self.copy_right()
            elif self.right.is_empty():
                self.copy_left()
            else:
                replacement = self.right.find_min()
                self.right.delete(replacement)
                self.val = replacement

    def make_empty(self):
        self.val = None
        self.left = None
        self.right = None

    def copy_right(self):
        right = self.right
        self.val = right.val
        self.left = right.left
        self.right = right.right

    def copy_left(self):
        left = self.left
        self.val = left.val
        self.left = left.left
        self.right = left.right

    def find_min(self):
        if self.left.is_empty():
            return self.val
        return self.left.find_min()
    
    def height(self):
        if self.is_empty():
            return -1
        return 1 + max(self.left.height(), self.right.height())
    
    def num_nodes(self):
        if self.is_empty():
            return 0
        return 1 + self.left.num_nodes() + self.right.num_nodes()
    

class BST:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        self.root.insert(key)

    def delete(self, key):
        self.root.delete(key)

    def height(self):
        return self.root.height()

    def number_of_nodes(self):
        return self.root.num_nodes()

    def inorder(self):
        result = []
        def visit(node: Node):
            if node.is_empty():
                return
            visit(node.left)
            result.append(node.val)
            visit(node.right)
        visit(self.root)
        return result

    def preorder(self):
        result = []
        def visit(node: Node):
            if node.is_empty():
                return
            result.append(node.val)
            visit(node.left)
            visit(node.right)
        visit(self.root)
        return result

    def postorder(self):
        result = []
        def visit(node: Node):
            if node.is_empty():
                return
            visit(node.left)
            visit(node.right)
            result.append(node.val)
        visit(self.root)
        return result


def process_file(filename):
    tree = BST()
    out = []
    with open(filename, encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            p = line.split()
            cmd = p[0].upper()
            if cmd == 'I': tree.insert(int(p[1]))
            elif cmd == 'D': tree.delete(int(p[1]))
            elif cmd == 'H': out.append(str(tree.height()))
            elif cmd == 'N': out.append(str(tree.number_of_nodes()))
            elif cmd == 'IN': out.append(' '.join(map(str, tree.inorder())))
            elif cmd == 'PRE': out.append(' '.join(map(str, tree.preorder())))
            elif cmd == 'POST': out.append(' '.join(map(str, tree.postorder())))
            else: raise ValueError(f'Unknown command: {cmd}')
    return out

def main():
    if len(sys.argv) != 2:
        print('Usage: python bst.py test.txt')
        sys.exit(2)
    print('\n'.join(process_file(sys.argv[1])))

if __name__ == '__main__':
    main()
