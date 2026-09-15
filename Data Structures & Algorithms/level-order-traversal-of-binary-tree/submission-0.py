# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This is just gonna be BFS with maybe one slight trick to it
        # BFS (iterative):
        if not root:
            return []
        ans = []
        nodes = deque([root])
        n = 0
        while nodes:
            res = []
            for i in range(0, len(nodes)):
                curr = nodes.popleft()
                res.append(curr.val)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
            ans.append(res)
        return ans