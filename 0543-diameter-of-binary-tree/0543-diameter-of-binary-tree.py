# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def __init__(self):
    #     self.m=0
    # def h(self,root):
    #     if not root:
    #         return 0
    #     l=self.h(root.left)
    #     r=self.h(root.right)
    #     if l+r>self.m:
    #         self.m=l+r
    #     # if l>r:
    #     #     return l+1
    #     return max(r,l)+1
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.m=0
        def h(root):
            if not root:
                return 0
            l=h(root.left)
            r=h(root.right)
            if l+r>self.m:
                self.m=l+r
            return max(r,l)+1
        h(root)
        return self.m