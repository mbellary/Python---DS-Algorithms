class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Test case
# 1
#         0
#       /   \
#      1     2
#    /   \
#   3    4

root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
root.left = one
root.right = two
one.left = three
one.right = four

print(root.left.left.val)
print(root.right.val)