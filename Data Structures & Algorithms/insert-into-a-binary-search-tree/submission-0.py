# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return TreeNode(val, None, None)

        print(f"Current node is {root.val}")


        if val < root.val: 
            print(f"{val} < {root.val} so going left")
            x = self.insertIntoBST(root.left,val)
            root.left = x

        if val > root.val:
            print(f"{val} > {root.val} so going right")
            x = self.insertIntoBST(root.right,val)
            root.right = x

        return root
        

# use the recursive calls return value 
# the recursive call returns a root 
        # base case is that if there is no root, then the value to be inserted
            # becomes the root. so return val 
        
        # need to iterate through the tree and check whether the node to be inserted
            # is less than or more than the current node.

        # once we reach a leaf node we check whether the node to be inserted is less
            # than or more than the leaf, and assign the val respectively
            # val = node.left or val = node.right

        # i am mixing alot of node and val words together which isnt consistent
        # but you get the idea 

# 1.) create the base case. if there is no root than val becomes a node (root)
# 2.) val is smaller / larger logic 
        