# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If both p and q are less than curr node val -> in left subtree
        # If both p and q greater than curr node val -> right subtree
        # If even one of them is the curr node val -> return the curr node
        # If one isn't greater than the curr node/one is less -> return curr node
        # cuz that means they diverse from that node
        # First 2 require custom ifs
        # Last 2 can be in a 'catch-all' else
        if not root or not p or not q:
            return None
        if (max(p.val, q.val)<root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root