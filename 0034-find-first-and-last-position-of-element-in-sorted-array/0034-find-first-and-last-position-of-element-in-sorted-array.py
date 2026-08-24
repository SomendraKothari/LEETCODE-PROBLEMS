class Solution(object):
    def ub(self,n,t):
        l=0
        r=len(n)-1
        ans=r+1
        while l<=r:
            m=(l+r)//2
            if n[m]>t:
                r=m-1
                ans=m
            else:
                l=m+1
        return ans
    def lb(self,n,t):
        l=0
        r=len(n)-1
        ans=r+1
        while l<=r:
            m=(l+r)//2
            if n[m]>=t:
                r=m-1
                ans=m
            else:
                l=m+1
        return ans
    def searchRange(self, n, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lb=self.lb(n,t)
        ub=self.ub(n,t)
        if ub==lb:
            return [-1,-1]
        return [lb,ub-1]