import heapq
class Solution(object):
    def lastStoneWeight(self,s):
        """
        :type stones: List[int]
        :rtype: int
        """
        h=[]
        for i in s:
            heapq.heappush(h,-i)
        while len(h)>1:
            x=-heapq.heappop(h)
            y=-heapq.heappop(h)
            if x!=y:
                heapq.heappush(h,y-x)
        if len(h)==0:
            return 0
        return -h[0]