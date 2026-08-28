# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 
class Queue(object):
    def __init__(self):
        self.q=[]
        self.front=-1
    def push(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            return -1
        x=self.q[self.front]
        self.front+=1
        if self.front==len(self.q):
            self.q=[]
            self.front=-1
        return x
    def size(self):
        if self.front==-1:
            return 0
        return len(self.q)-self.front
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        if root==None:
            return ans
        q=Queue()
        q.push(root)
        ans.append([root.val])
        while q.size()>0:
            l=q.size()
            lev=[]
            for i in range(l):
                x=q.pop()
                if x.left:
                    q.push(x.left)
                    lev.append(x.left.val)
                if x.right:
                    q.push(x.right)
                    lev.append(x.right.val)
            if len(lev)!=0:
                ans.append(lev)
        return ans