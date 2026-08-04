class Solution(object):
    def topKFrequent(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in n:
            d[i]=d.get(i,0)+1
        l=[[] for i in range(len(n)+1)]
        for i,j in d.items():
            l[j].append(i)
        ans=[]
        for i in range(len(n),0,-1):
            for j in l[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans