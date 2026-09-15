# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # input: root of a bin tree
        # output: the nodes that are visible from the right side of the tree
        # constraint: when we say 'visible', we mean that we want to return the 
        #             nodes that have no other nodes to the right of them at their
        #             level in the tree

        # first set up bfs algo 

        if not root:
            return []
        ans = []
        q = deque([root])
        while q: 
            for i in range(0, len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right: # We want to somehow get the node that is to the farthest right
                    q.append(curr.right)
            ans.append(curr.val)

        return ans