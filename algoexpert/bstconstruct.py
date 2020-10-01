class BST:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
    def insert(self,value):
        currentnode = self
        
        while True:
            if value<currentnode.value:
                if currentnode.left is None:
                    currentnode.left = BST(value)
                    break
                else:
                    currentnode = currentnode.left
            else:
                if currentnode.right is None:
                    currentnode.right = BST(value)
                    break
                else:
                    currentnode = currentnode.right
        return self

    def inorder(self,tree,array):
            
        if tree is not None:
            inorder(tree.left,array)
            array.append(tree.value)
            inorder(tree.right,array)
        return array
            

            
tree = BST(3)
tree.insert(5)
tree.insert(7)
tree.insert(8)
tree.inorder(tree)
print(y)
