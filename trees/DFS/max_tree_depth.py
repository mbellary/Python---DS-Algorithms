from typing import Optional
from trees.node.TreeNode import TreeNode


def max_depth_recursion(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    left = max_depth_recursion(node.left)
    right = max_depth_recursion(node.right)

    return max(left, right) + 1

def max_depth_iter(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    ans = 0
    stack = [(root, 1)]

    while stack:
        node, depth = stack.pop()
        ans = max(ans, depth)

        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    return ans

# Test Case
node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
root = node0
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
node5.right = node6

recur_result = max_depth_recursion(root)
iter_result = max_depth_iter(root)
assert (recur_result == iter_result)

print(f'Recursion => max depth of the tree is {recur_result}')
print(f'Iteratively => max depth of the tree is {iter_result}')
