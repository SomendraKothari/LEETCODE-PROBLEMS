class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        x=0
        while x<n/2:
            s[x] , s[n-1-x] = s[n-1-x] , s[x]
            x+=1