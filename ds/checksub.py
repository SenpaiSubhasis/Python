class BST:
  def __init__(self,value):
    self.value = value
    self.right = None
    self.left = None

def inorder(tree_1_2,store_1):
  if tree_1_2:
    inorder(tree_1_2.left , store_1)
    store_1.append(tree_1_2.value)
    inorder(tree_1_2.right,store_1)

def postorder(tree_1_2,store_2):
  if tree_1_2:
    postorder(tree_1_2.left , store_2)
    postorder(tree_1_2.right,store_2)
    store_2.append(tree_1_2.value)


def toString(s):
  return str(s).replace("[","").replace("]","")


def isSubtree(tree_1,tree_2):
  if tree_1 == None:
    return True
  if tree_2 == None:
    return False
  
  first_array = []
  second_array = []

  inorder(tree_1 , first_array)
  inorder(tree_2 , second_array)

  if toString(first_array).find(toString(second_array))== -1:
    return False
  first_array.clear()
  second_array.clear()

  postorder(tree_1 , first_array)
  postorder(tree_2 , second_array)

  if toString(first_array).find(toString(second_array))== -1:
    return False

  return True


if __name__ == "__main__":
  root_A = BST("a")
  root_A.left = BST("b")
  root_A.right = BST("d")
  root_A.left.left = BST("c")
  root_A.right.right = BST("e")
  
  root_B = BST("a")
  root_B.left = BST("b")
  root_B.left.left = BST("c")
  root_B.right = BST("d")

  if isSubtree(root_A,root_B):
    print(1)
  else:
    print(-1)


  