from typing import Optional
from trees.node.TreeNode import TreeNode

def path_sum_recursion(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(node, curr):
        if not root:
            return False

        if root.left == None and root.right == None:
            return (curr + root.val) == targetSum

        curr += root.val
        left = dfs(root.left, curr)
        right = dfs(root.right, curr)
        return left or right

    return dfs(root, 0)


def path_sum_iter(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    stack = [(root, 0)]
    while stack:
        node, curr = stack.pop()

        if node.left == None and node.right == None:
            return (curr + node.val) == targetSum

        curr += node.val
        if node.left:
            stack.append((node.left, curr))
        if node.right:
            stack.append((node.right, curr))

    return False