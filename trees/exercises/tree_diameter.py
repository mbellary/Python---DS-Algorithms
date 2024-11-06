from typing import Optional
from trees.node.TreeNode import TreeNode


def dfs(root: Optional[TreeNode]):
    if not root:
        return 1
    ans = 0
    ans += dfs(root.left)
    ans += dfs(root.right)

    # if not parent:
    #     print(f'{left} - {right}')
    #     return max( max(left, right) , left + right)

    return ans

# Test Case
#1
node1 = TreeNode(1)
node2 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(5)
node3 = TreeNode(3)

root = node1
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5

result = dfs(root)
print(f"Diameter of Binary Tree is : {result}")

#1
node1 = TreeNode(1)
node2 = TreeNode(2)
root = node1
root.left = node2

result = dfs(root)
print(f"Diameter of Binary Tree is : {result}")

#2
node1 = TreeNode(1)
root = node1
result = dfs(root)
print(f"Diameter of Binary Tree is : {result}")