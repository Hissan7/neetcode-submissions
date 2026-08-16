"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = [] # array to insert values into during the traversal

        # helper function 
        def post(node):
            
            if node is None: # base case 
                return 
            
            # if node.children: # if the list of nodes isnt empty

            for child in node.children: # iterate through each node in the list
                post(child) # i dont know if this is in the right place
            res.append(node.val)


#node.children is a list of nodes 
# we need to append the children of the parent and then the parent at the end 

        post(root) # entry point 
        return res