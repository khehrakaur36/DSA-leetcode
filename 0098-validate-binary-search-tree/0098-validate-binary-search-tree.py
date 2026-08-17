# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def fun(root, left, right):  
            if root is None:
                return True
            if root.val<= left or root.val>=right:
                return False
            return fun(root.left, left , root.val) and fun(root.right , root.val , right)
        return fun(root, float("-inf") , float("inf"))        
