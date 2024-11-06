from collections import deque
from trees.node.TreeNode import TreeNode
from typing import Optional


def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    queue = deque([root])
    ans = []


    while queue:
        curr = 0
        current_length = len(queue)

        for _ in range(len(queue)):
            node = queue.popleft()
            curr += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    ans.append(curr)

    return ans[-1]

