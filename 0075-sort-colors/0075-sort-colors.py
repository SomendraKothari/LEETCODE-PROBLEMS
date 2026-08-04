class Solution(object):
    def sortColors(self, n):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=z=0
        r=len(n)-1
        while l<r:
            if n[l]==2:
                n[l],n[r]=n[r],n[l]
                while l<r and n[r]==2:
                    r-=1
                # ab r waha jaha 0 ya 1
            elif n[l]==0:
                if l>z:
                    n[l],n[z]=n[z],n[l]
                    z+=1
                else:
                    l+=1
            else:
                if n[r]==0:
                    n[r],n[z]=n[z],n[r]
                    z+=1
                else:
                    l+=1
        