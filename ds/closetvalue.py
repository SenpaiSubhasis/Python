class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


def closest(tree , target):
    return findtheClosestValue(tree, target , float("inf"))

def findtheClosestValue(tree , target , closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findtheClosestValue(tree.left , target , closest)
    elif target > tree.value:
        return findtheClosestValue(tree.right , target , closest)
    else:
        return closest

tree = BST(10)
tree.left = BST(5)
tree.left.right = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.right = BST(15)
tree.right.left = BST(13)
tree.right.right = BST(22)
tree.right.left.right = BST(14)
ans = closest(tree ,12)
print(ans)