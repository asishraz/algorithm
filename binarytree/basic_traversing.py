'''

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

#           1
#         /   \
#        2     3
#       / \   / \
#      4   5  6  7


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
'''
##################################################################

class Node:
     def __init__(self,value):
          self.value = value
          self.left = None
          self.right = None


class BinaryTree:
     def __init__(self,root):
          self.root = Node(root)
          


tree = BinaryTree()
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


