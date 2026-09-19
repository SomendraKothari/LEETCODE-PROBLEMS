# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, t):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # self.ans=False
        # def check(root,s):
        #     if not root:
        #         return 0
        #     if self.ans:
        #         return
        #     s+=root.val
        #     l=check(root.left,s)
        #     r=check(root.right,s)
        #     if l==0 and r==0 and s==t:
        #         self.ans=True
        # check(root,0)
        # return self.ans

        if not root:
            return False
        if not root.left and not root.right:
            return t==root.val
        rem=t-root.val
        return self.hasPathSum(root.left,rem) or self.hasPathSum(root.right,rem)