# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    # we start at the root 
    # assuming this is some recursive thing 
    # usually to find the length of the tree we use DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1+max(left_depth,right_depth)
    


    #start from the root 
    # if the root has no children then stop
    # else go to the left and check if the child node also has children 
    # add 1 to a counter ? 
        
        