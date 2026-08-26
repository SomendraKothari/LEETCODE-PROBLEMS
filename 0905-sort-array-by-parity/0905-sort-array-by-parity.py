class Solution(object):
    def sortArrayByParity(self, n):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=len(n)-1
        i=0
        while i<r:
            if n[i]%2!=0:
               n[r],n[i]=n[i],n[r]
               r-=1
            else:
                i+=1
        return n