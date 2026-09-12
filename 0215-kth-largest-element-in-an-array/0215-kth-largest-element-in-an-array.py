class Solution(object):
    def findKthLargest(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n.sort()
        return n[-k]