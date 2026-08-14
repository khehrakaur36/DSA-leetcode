# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res =[]
        def fun(root , cursum, path):
            if root is None:
                return 
            cursum += root.val
            path.append(root.val)

            if root.left is None and root.right is None:
                if cursum == targetSum:
                    res.append(path.copy())
            fun(root.left , cursum , path)
            fun(root.right , cursum , path)

            path.pop()
        fun(root , 0, [])
        return res              
