# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        nn=TreeNode(val)
        if not root:
            return nn
        cur=root
        while cur:
            if cur.val<val:
                if not cur.right:
                    cur.right=nn
                    break
                cur=cur.right
            else:
                if not cur.left:
                    cur.left=nn
                    break
                cur=cur.left
        return root