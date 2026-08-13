# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        asc=[]
        desc=[]
        def getsmall():
            while root:
                asc.append(root)
                root=root.left
        def getbig():
            while root:
                desc.append(root)
                root = root.right

        node = root
        while node:
            asc.append(node)
            node = node.left

        node=root
        while node:
            desc.append(node)
            node= node.right

        i=asc.pop()
        j=desc.pop()

        while i != j and i.val<j.val:
            total = i.val + j.val
            if total==k:
                return True

            if total <k:
                node= i.right
                while node:
                    asc.append(node)
                    node= node.left


                if not asc:
                    break
                i= asc.pop()
            else:
                node = j.left
                while node:
                    desc.append(node)
                    node = node.right
                if not desc:
                    break
                j= desc.pop()
        return False                                                                