class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self,value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
 


def printPreorder(root):
    if root:
        print(root.value)
        printPreorder(root.left)
        printPreorder(root.right)

def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.value), 
  
        # now recur on right child 
        printInorder(root.right) 
  
  

 
 
 
r = BST(1)
x = r.insert(3).insert(2).insert(7).insert(6).insert(9).insert(13)
 
 
printf = printInorder(r)
print(printf)