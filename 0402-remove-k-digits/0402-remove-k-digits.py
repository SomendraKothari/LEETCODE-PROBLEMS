class Solution(object):
    def removeKdigits(self, n, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # l=len(n)
        # if k>=l:
        #     return "0"
        # sa=[]
        # for i in range(l):
        #     if k<=0:
        #         sa.append(n[i])
        #         continue
        #     if sa and sa[-1]<n[i]:
        #         k-=1
        #         continue
        #     elif sa and sa[-1]>n[i]:
        #         while sa and sa[-1]>n[i] and k>0:
        #             sa.pop()
        #             k-=1
        #     sa.append(n[i])
        # ans=""
        # for i in sa:
        #     ans+=i
        # c=0
        # l1=len(ans)
        # while c<l1 and ans[c]=="0":
        #     c+=1
        # if l1==0 or c==l1:
        #     return "0"
        # if k>0:
        #     c+=k
        # return ans[c:]

        sa = []
        for i in n:
            while sa and k > 0 and sa[-1] > i:
                sa.pop()
                k -= 1
            sa.append(i)
    
    # Agar k abhi bhi bacha ho toh last se pop karein
        sa = sa[:-k] if k > 0 else sa
    
    # Leading zeros remove karein
        res = "".join(sa).lstrip("0")
        return res if res else "0"