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

        res = []
        def dfs(root):
            if not root: 
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        ans = float("inf")
        for i in range(k):
            ans = res[i]
        return ans
        