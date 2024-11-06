from trees.node.TreeNode import TreeNode
from typing import Optional
from collections import deque

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        root = TreeNode(val)

    def dfs(root: Optional[TreeNode], val: int):

        if not root:
            return None

        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            left = dfs(root.left, val)
        if root.val < val:
            if not root.right:
                root.right = TreeNode(val)
            right = dfs(root.right, val)
        return root

    return dfs(root, val)

def printResults(root: Optional[TreeNode]):
    queue = deque([root])
    ans = []
    while queue:
        curr_len = len(queue)

        for _ in range(curr_len):
            node = queue.popleft()
            ans.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

# Test Case
# 1
node4 = TreeNode(4)
node2 = TreeNode(2)
node1 = TreeNode(1)
node3 = TreeNode(3)
node7 = TreeNode(7)

root = node4
root.left = node2
root.right = node7
node2.left = node1
node2.right = node3
result = insertIntoBST(root, 5)
ans = printResults(result)
print(ans)

# 1
node40 = TreeNode(40)
node20 = TreeNode(20)
node60 = TreeNode(60)
node10 = TreeNode(10)
node30 = TreeNode(30)
node50 = TreeNode(50)
node70 = TreeNode(70)

root = node40
root.left = node20
root.right = node60
node20.left = node10
node20.right = node30
node60.left = node50
node60.right = node70
result = insertIntoBST(root, 25)
ans = printResults(result)
print(ans)