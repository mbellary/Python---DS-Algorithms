from collections import deque
from trees.node.TreeNode import TreeNode
from typing import Optional

def zigzagLevelOrder(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    queue = deque([root])
    ans = []
    order = "LR"

    while queue:
        elements = []
        curr_len = len(queue)

        for _ in range(curr_len):
            node = queue.popleft()
            elements.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if order == "LR":
            ans.append(elements)
            order = "RL"
        else:
            order = "LR"
            elements.reverse()
            ans.append(elements)

    return ans

# Test Case
# 1
node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

root = node3
root.left = node9
root.right = node20
node20.left = node15
node20.right = node7

result = zigzagLevelOrder(root)
print(f'zigzag result is : {result}')