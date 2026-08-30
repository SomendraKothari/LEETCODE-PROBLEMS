# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        cur=root
        if cur.val<key:
            cur.right=self.deleteNode(cur.right,key)
        if cur.val>key:
            cur.left=self.deleteNode(cur.left,key)
        if cur.val==key:
            if not cur.left and not cur.right:
                return None
            elif not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left
            else:
                l=cur.right
                while l.left:
                    l=l.left
                cur.val=l.val
                cur.right=self.deleteNode(cur.right,l.val)
        return root