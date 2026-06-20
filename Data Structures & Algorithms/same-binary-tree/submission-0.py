# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#if 1 = 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #if both trees roots dont have children
            return True
        if not p or not q: #if atleast one of the trees roots dont have children
            return False 
        if p.val != q.val: #if the nodes value in tree_p is not the same as the nodes value in tree_
            return False 

        return(self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

