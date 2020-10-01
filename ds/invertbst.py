class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def invert(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left,tree.right = tree.right,tree.left

def printPreorder(root):
    if root:
        print(root.value)
        printPreorder(root.left)
        printPreorder(root.right)

tree = BST(1)
tree.left = BST(2)
tree.right = BST(3)
tree.left.left = BST(4)
tree.left.right = BST(5)
tree.right.left = BST(6)
tree.right.right = BST(7)
ans = invert(tree)
x = printPreorder(tree)
print(x)
