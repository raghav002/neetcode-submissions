# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # input: the root of a binary tree
        # output: the length of the longest path between any two nodes in a tree
        # constraints: length of a path between two nodes is the number of edges
        #              between the nodes. The path cannot include same node twice

        dia = 0
        def dfs(node):
            nonlocal dia
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            dia = max(dia, right + left)
            return max(left, right) + 1 
        dfs(root)
        return dia
        