class Solution(object):
    def findPeakElement(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(n)-1
        while l<r:
            m=l+(r-l)//2
            if n[m]<n[m+1]:
                l=m+1
            else:
                r=m
        return l