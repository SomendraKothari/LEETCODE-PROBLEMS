class Solution(object):
    def peakIndexInMountainArray(self, a):
        """
        :type arr: List[int]
        :rtype: int
        """
        l=0
        r=len(a)-1
        while l<r:
            m=(r+l)//2
            if a[m]<a[m+1]:
                l=m+1
            else:
                r=m
        return l