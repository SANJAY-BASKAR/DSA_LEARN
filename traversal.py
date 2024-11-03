class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print("In-order:", end=" ")
inorder(root)     # Output: 2 1 3
print("\nPre-order:", end=" ")
preorder(root)    # Output: 1 2 3
print("\nPost-order:", end=" ")
postorder(root)   # Output: 2 3 1
