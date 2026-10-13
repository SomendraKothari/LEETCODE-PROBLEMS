class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n=0
        ne=True
        if x<0:
            ne=False
            x=-x
        while x>0:
            n=n*10+x%10
            x//=10
        if n>2147483647:
            return 0
        if ne:
            return n
        return -n