class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example: Create a simple tree
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
