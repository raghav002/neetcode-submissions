# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Let's try to do traversal first:
        # Traversal steps:
        # Put the root into a queue.
        # While the queue exists
        # pop out the current node. Print the value
        # If it has a left/right child, enqueue them,
        # continue
        if not root:
            return
        test = deque([root])
        while test:
            curr = test.popleft()
            print(curr.val)
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                test.append(curr.left)
            if curr.right:
                test.append(curr.right) 
        return root
        
        