class Solution(object):
    def twoSum(self, n, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        d={}
        for i in range(len(n)):
            s=t-n[i]
            if s in d:
                return [i,d[s]]
            d[n[i]]=i