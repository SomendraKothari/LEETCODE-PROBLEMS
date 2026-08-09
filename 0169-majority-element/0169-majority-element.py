class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        for i in list(set(nums)):
            if nums.count(i) > l/2:
                return i