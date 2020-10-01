class BST:
    def __init__(self,value):
        self.value  = value
        self.right = None
        self.left = None


def validate_BST(tree):
    return validateBstHelper(tree,float("-inf"),float("inf"))

def validateBstHelper(tree,minValue,maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value>=maxValue:
        return False
    leftSide = validateBstHelper(tree.left , minValue , tree.value)
    return leftSide and validateBstHelper(tree.right,tree.value,maxValue)



tree = BST(4)
tree.left = BST(2)
tree.right = BST(7)
tree.left.left = BST(1)
tree.left.right = BST(3)
tree.right.left = BST(6)
tree.right.right = BST(9)
ans = validate_BST(tree)
print(ans)