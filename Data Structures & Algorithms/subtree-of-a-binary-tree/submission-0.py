# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # input: two root nodes - one for root the other subroot
        # output: if subroot is a subtree of root 
        # key things to consider: 
        #   a tree can be considered as a subtree of itself
        # When solving it with a human approach, we technically go through each node, waiting
        # for the first point at which we see a similarity
        # When we reach that similarity, from that point we start comparing the tree 

        # I think dfs or bfs works here... not sure which one to use entirely, but let's see

        def compareTrees(root, subroot):
            # Dfs again?
            if not root and not subroot:
                return True
            if not root and subroot:
                return False
            if not subroot and root:
                return False
            if subroot.val != root.val:
                return False
            left = compareTrees(root.left, subroot.left)
            right = compareTrees(root.right, subroot.right)
            state = left and right 
            return state
        
        def dfs(node):
            if not node:
                return False # this means no match found until this point
            # We're doing a pre-order approach in some sense
            if node.val == subRoot.val: # we have to get a node with same val as subroot's root
                # Do a comparison from that point
                state = compareTrees(node, subRoot)
                if state: return True
            else:
                state = False
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right
        
        if not subRoot:
            return False
        # Begin going through root
        ans = dfs(root)
        return ans

        