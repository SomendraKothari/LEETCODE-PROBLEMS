class Solution(object):
    def findMin(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(n)==1:
            return n[0]
        l=0
        r=len(n)-1
        mi=5001
        while l<=r:
            m=(r+l)//2
            if n[l]<=n[m]:
                mi=min(mi,n[l])
                l=m+1
            else:
                r=m
        return mi