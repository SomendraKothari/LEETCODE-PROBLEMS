class Solution(object):
    def topKFrequent(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # d={}
        # for i in n:
        #     d[i]=d.get(i,0)+1
        # l=[[] for i in range(len(n)+1)]
        # for i in d.items():
        #     l[i[1]].append(i[0])
        # ans=[]
        # for i in range(len(n),0,-1):
        #     for m in l[i]:
        #         ans.append(m)
        #         if len(ans)==k:
        #             return ans


        # d={}
        # for i in n:
        #     d[i]=d.get(i,0)+1
        # # d={1:3,2:2,3:1}
        # l=[]
        # for _ in range(len(n)+1):
        #     l.append([])
        # for i,j in d.items():
        #     l[j].append(i)
        # r=[]
        # for i in range(len(n),0,-1):
        #     for j in l[i]:
        #         r.append(j)
        #         if len(r)==k:
        #             return r


        d={}
        for i in n:
            d[i]=d.get(i,0)+1
        l=[[] for i in range(len(n)+1)]
        for i,m in d.items():
            l[m].append(i)
        ans=[]
        for i in range(len(n),0,-1):
            for j in l[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans