# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], result = None) -> bool:
        r1 = self.preorder(root)
        r2 = self.preorder(subRoot)
        if r2 in r1:
            return True
        return False

    def preorder(self,root):
        result = ""
        
        def dfs(node):
            nonlocal result


            if not node:
                result += "#"
                return

            result += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
        
        # entry point 
        dfs(root)
        return result
            

            

            
            
            