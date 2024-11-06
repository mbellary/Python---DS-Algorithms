from collections import deque
from typing import Optional
from trees.node.TreeNode import TreeNode

def RightSideView(root: Optional[TreeNode]):
    queue = deque([root])
    ans = []

    while queue:
        current_length = len(queue)
        ans.append(queue[-1].val)

        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return ans

