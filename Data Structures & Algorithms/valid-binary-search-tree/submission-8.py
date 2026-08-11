# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# valid binary search tree criteria : 
# root node cannot be more than right node or less than left node 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            # base case: what should happen if node is None?
            if not node:
                return True

            # what should happen if node.val is NOT strictly between low and high?
            if not (low < node.val < high):
                return False

            # recurse into both children with updated bounds
            # what are the new low/high for the left child?
            # what are the new low/high for the right child?
            return valid(node.left,low,node.val) and valid(node.right,node.val,high)

        return valid(root, float('-inf'), float('inf'))


