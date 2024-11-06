# Pending:
# How to efficiently trace the path of a node.

from trees.node.TreeNode import TreeNode
from typing import Optional


# def maxAncestorDiff(root: Optional[TreeNode]) -> int:
#     def dfs(root, val, visited, head):
#         if not root:
#             return 0
#
#         max_val = val
#         seen = visited
#         ancestor = head
#
#         if seen:
#             for i in range(len(seen)):
#                 abs_diff = abs(root.val - seen[i])
#                 if abs_diff >= max_val:
#                     max_val = abs_diff
#
#         if root.left or root.right:
#             seen.append(root.val)
#
#         if not seen:
#             seen.append(root.val)
#
#         # print(seen)
#         left = dfs(root.left, max_val, seen, ancestor)
#         if root.right == ancestor.right:
#             seen = [ancestor.val]
#         right = dfs(root.right, max_val, seen, ancestor)
#
#         return max(left, right, max_val)
#
#     return dfs(root, 0, [], root)

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    def dfs(root, parent_max, parent_min, parent_diff):
        if not root:
            return 0

        node_max = max(root.val, parent_max)
        node_min = min(root.val, parent_min)
        node_diff = abs(node_max - node_min)
        max_val = max(parent_diff, node_diff)

        left = dfs(root.left, node_max, node_min, max_val)
        right = dfs(root.right, node_max, node_min, max_val)

        return max( left, right, max_val)

    return dfs(root, root.val, root.val, 0)


# Test Case
# 1
node0 = TreeNode(8)
node1 = TreeNode(3)
node2 = TreeNode(10)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(14)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(13)

root = node0
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node4.left = node6
node4.right = node7
node2.right = node5
node5.left = node8

result = maxAncestorDiff(root)
print(f'maximum difference between node and ancestor is : {result}')

# 2
node1 = TreeNode(1)
node2 = TreeNode(2)
node0 = TreeNode(0)
node3 = TreeNode(3)

root = node1
root.right = node2
node2.right = node0
node0.left = node3

result = maxAncestorDiff(root)
print(f'maximum difference between node and ancestor is : {result}')

# 3 [Failed Test Case]
# input [4,7,2,3,9,null,null,12,null,0,null,null,6,null,null,null,8,null,11,null,10,1,null,5]
node4 = TreeNode(4)
node7 = TreeNode(7)
node2 = TreeNode(2)
node3 = TreeNode(3)
node9 = TreeNode(9)
node12 = TreeNode(12)
node0 = TreeNode(0)
node6 = TreeNode(6)
node8 = TreeNode(8)
node11 = TreeNode(11)
node10 = TreeNode(10)
node1 = TreeNode(1)
node5 = TreeNode(5)

root = node4
root.left = node7
node4.right = node2
node7.left = node3
node7.right = node9
node9.left = node0
node3.left = node12
node12.right = node6
node6.right = node8
node8.right = node11
node11.right = node10
node10.left = node1
node1.left = node5

result = maxAncestorDiff(root)
print(f'maximum difference between node and ancestor is : {result}')
