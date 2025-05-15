class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node: return Node(value)
            if value < node.value: node.left = _insert(node.left, value)
            elif value > node.value: node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node or node.value == value: return node
            if value < node.value: return _search(node.left, value)
            return _search(node.right, value)
        return _search(self.root, value)

    def in_order_traversal(self):
        result = []
        def _in_order(node):
            if node:
                _in_order(node.left)
                result.append(node.value)
                _in_order(node.right)
        _in_order(self.root)
        return result

tree = BST()
for val in [50, 30, 70, 20, 40, 60, 80]: tree.insert(val)
print(tree.in_order_traversal())
while True:
    target = int(input('Input target: '))
    found = tree.search(target)
    print("Value found" if found else "Not found") #By B. Nazarzoda 241ADB013