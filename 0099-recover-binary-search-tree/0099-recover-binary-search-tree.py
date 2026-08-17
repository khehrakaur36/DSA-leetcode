# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        sec = None
        prev = None
        def fun(root):
            nonlocal first , sec, prev
            if root is None:
                return
            fun(root.left)
            if prev and prev.val>root.val:
                if first is None:
                    first = prev
                sec = root
            prev = root
            fun(root.right)
        fun(root)
        first.val , sec.val = sec.val , first.val                
        