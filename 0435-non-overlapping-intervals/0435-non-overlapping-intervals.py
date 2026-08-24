class Solution(object):
    def eraseOverlapIntervals(self, n):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n.sort(key=lambda x:x[1])
        l=len(n)
        p=c=0# c for overlapping ones
        for i in range(1,l):
            if n[i][0]<n[p][1]:
                c+=1
            else:
                p=i
        return c