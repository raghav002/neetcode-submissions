# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # input: the root of a tree
        #        two nodes p and q
        # output: the LCA of p and q
        # constraint: LCA = the lowest node in tree T such that both are descendants
        #             the ancestor is allowed to be a descendant of itself
        # unique properties of problem: all BST values are unique 

        # 3 cases:
        # root is p or q -> Root is the answer
        # p and q are in left and right subtree (rooted at root) -> root is the answer
        # p and q are in a subtree (find the LCA)

        if not root:
            return None
            
        if root == q or root == p:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right
        