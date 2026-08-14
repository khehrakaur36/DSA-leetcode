# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fun(root , cursum):
            if root is None:
                return False
            cursum+= root.val
            if root.left is None and root.right is None:
                return  cursum == targetSum
            return fun(root.left , cursum) or fun(root.right , cursum)     
        return fun(root ,0)