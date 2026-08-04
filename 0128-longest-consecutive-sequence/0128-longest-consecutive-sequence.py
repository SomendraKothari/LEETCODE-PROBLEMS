class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        m=0
        for i in s:
            if i-1 in s:
                continue
            c=1
            while i+c in s:
                c+=1
            m=max(m,c)
        return m