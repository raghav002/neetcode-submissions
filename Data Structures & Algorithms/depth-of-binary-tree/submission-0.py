# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # First define the traversal. If we're calcing max depth, conceptually the 
        # children are most important since they will indicate the max depth. So
        # logic here should probably be performed in a postorder method
        if root == None:
            return 0 # depth is an integer value
        leftD = self.maxDepth(root.left)
        rightD = self.maxDepth(root.right)
        return max(leftD, rightD) + 1 # Plus 1 since the base case returns 0

        