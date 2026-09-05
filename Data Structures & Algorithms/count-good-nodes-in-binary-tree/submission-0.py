# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # input: a binary tree root - root
        # output: the number of good nodes in the tree
        # constraint: a good node x is such if the path from root to node x has no
        #             values greater than x 
        #             if the values of all nodes from node root to x are less than <=x
        #             x is a good node
        def dfs(node, maxSF):
            if not node:
                return 0
            left = dfs(node.left, max(maxSF, node.val))
            right = dfs(node.right, max(maxSF, node.val))
            ans = left + right
            if node.val>=maxSF:
                ans+=1
            return ans

        return dfs(root, float("-inf"))
        