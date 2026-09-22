# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # input: Root of a BST root; integer k
        # output: the kth smallest integer in the tree
        # constraints: tree is 1-indexed;

        # Dumb way: DFS, add everything in (in-order traversal), badboom

        cnt = 0
        res = None
        def dfs(root):
            nonlocal res, cnt
            if not root or res is not None: 
                return
            dfs(root.left)
            cnt = cnt + 1
            if cnt == k:
                res = root.val
            dfs(root.right)
        dfs(root)
        return res
        