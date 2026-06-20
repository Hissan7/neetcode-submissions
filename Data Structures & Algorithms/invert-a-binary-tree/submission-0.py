# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root_list = []
        """
        well inverting a tree is making sure that for every 
        node, the children of it are swapped 

        so originally if node.left = 2 and node.left = 3
        now it should be node.left = 3 and node.right = 2
        """

        """
        if there is no node:
            stop
        
        go left and get the left node 
        go right and get the right node 

        """

        if not root:
            return 

        #swapping the children of the node
        root.left, root.right = root.right, root.left 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 



        