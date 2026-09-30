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
        # TODO: implement insertion
        self.root=self._insert(self.root,key)
    def _insert(self,node,key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left= self.insert(self.left,key)
        elif key>node.key:
            node.right=self.insert(self.right,key)
        return node
    
    


        pass

    def delete(self, key):
        # TODO: implement deletion
        pass

    def height(self):
        # TODO: implement height
        # Height is measured in edges. Empty tree = -1.
        pass

    def number_of_nodes(self):
        # TODO: implement number of nodes
        pass

    def inorder(self):
        # TODO: implement inorder traversal
        pass

    def preorder(self):
        # TODO: implement preorder traversal
        pass

    def postorder(self):
        # TODO: implement postorder traversal
        pass


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
