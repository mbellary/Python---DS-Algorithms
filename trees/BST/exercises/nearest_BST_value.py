from typing import Optional
from trees.node.TreeNode import TreeNode


def closestValue(root: Optional[TreeNode], target: float) -> int:
    ans = []

    def dfs(root, node_val, curr_val):
        if not root:
            return 0

        if abs(root.val - target) < curr_val:
            curr_val = abs(root.val - target)
            node_val = root.val
            ans.append(node_val)
        elif abs(root.val - target) == curr_val:
            curr_val = abs(root.val - target)
            node_val = root.val
            if not ans:
                ans.append(node_val)
            elif node_val < ans[-1]:
                ans.pop()
                ans.append(node_val)


        if root.val > target:
            dfs(root.left, node_val, curr_val)
        if target > root.val:
            dfs(root.right, node_val, curr_val)

    dfs(root, root.val, float("inf"))
    return ans[-1]


# Test Case
# 1
node4 = TreeNode(4)
node2 = TreeNode(2)
node5 = TreeNode(5)
node1 = TreeNode(1)
node3 = TreeNode(3)

root = node4
root.left = node2
root.right = node5
node2.left = node1
node2.right = node3
result = closestValue(root, 3.714)
print(f'The closest node is {result}')

# 2
root = TreeNode(1)
result = closestValue(root, 4.42)
print(f'The closest node is {result}')

# 3
node1 = TreeNode(1)
node2 = TreeNode(2)
root = node1
root.right = node2
result = closestValue(root, 3.42)
print(f'The closest node is {result}')

# 4
node4 = TreeNode(4)
node2 = TreeNode(2)
node5 = TreeNode(5)
node1 = TreeNode(1)
node3 = TreeNode(3)

root = node4
root.left = node2
root.right = node5
node2.left = node1
node2.right = node3
result = closestValue(root, 3.5)
print(f'The closest node is {result}')

# 1
node4 = TreeNode(4)
node2 = TreeNode(2)
node5 = TreeNode(5)
node1 = TreeNode(1)
node3 = TreeNode(3)

root = node4
root.left = node2
root.right = node5
node2.left = node1
node2.right = node3
result = closestValue(root, 4.5)
print(f'The closest node is {result}')