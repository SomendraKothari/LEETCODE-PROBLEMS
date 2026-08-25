class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l=1
        # if x<=4:
        #     r=x
        # else:
        #     r=x//2
        r=x
        while l<=r:
            m=(l+r)//2
            if m*m>x:
                r=m-1
            else:
                l=m+1
        return l-1