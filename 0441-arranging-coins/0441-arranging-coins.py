class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=0
        r=n
        while l<r:
            m=l+(r-l)//2
            if m*(m+1)//2>n:
                r=m
            else:
                l=m+1
        if l*(l+1)//2>n:
            l=l-1
        return l