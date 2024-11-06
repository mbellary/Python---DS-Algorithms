from typing import Optional
from trees.node.TreeNode import TreeNode
def min_depth(root: Optional[TreeNode]) -> int :
    if not root:
        return 0

    left = min_depth(root.left)
    right = min_depth(root.right)

    if left == 0 or right == 0:  # when tree is fully left/right balanced
        return max(left, right) + 1

    return min(left, right) + 1

# Test Cases
# 1
node0 = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root = node0
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

result = min_depth(root)
print(f'min depth of the tree is {result}')

# 2
node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(6)

root = node0
root.right = node1
node1.right = node2
node2.right = node3
node3.right = node4

result = min_depth(root)
print(f'min depth of the tree is {result}')