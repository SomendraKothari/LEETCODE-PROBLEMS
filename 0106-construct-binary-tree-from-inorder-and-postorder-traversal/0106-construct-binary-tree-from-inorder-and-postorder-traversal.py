# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, i, p):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        l=len(p)
        d={}
        for i,v in enumerate(i):
            d[v]=i
        def check(ps,pe,si,ie):
            if ps>pe or si>ie:
                return None
            root=TreeNode(p[pe])
            ind=d[p[pe]] #4 , 3 , 1 , 0 , 2 , 6 , 
            il=ind-si # no of elements in left subtree
            root.left=check(ps,ps+il-1,si,ind-1)
            root.right=check(il+ps,pe-1,ind+1,ie)
            return root
        root = check(0,l-1,0,l-1)
        return root