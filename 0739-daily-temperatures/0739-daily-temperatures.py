class Solution(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # l=len(t)
        # s=[]
        # ans=[0]*l
        # ind=0
        # for i in range(l-1,-1,-1):
        #     if i<l-1 and t[i]==t[i+1]:
        #         if ans[i+1]==0:
        #             ans[i]=0
        #         else:
        #             ans[i]=ans[i+1]+1
        #         continue
        #     while len(s)>0 and s[-1]<=t[i]:
        #         s.pop()
        #     if not s:
        #         ans[i]=0
        #     else:
        #         while t[ind]!=s[-1]:
        #             ind+=1
        #         ans[i]=ind-i
        #     s.append(t[i])
        #     ind=i
        # return ans


        # l=len(t)
        # s=[]
        # ans=[0]*l
        # for i in range(l-1,-1,-1):
        #     while len(s)>0 and t[s[-1]]<=t[i]:
        #         s.pop()
        #     if s:
        #         ans[i]=s[-1]-i
        #     s.append(i)
        # return ans


        n = len(t)
        ans = [0] * n
        stack = []  # Stack mein indices rahenge

        for i, temp in enumerate(t):
        # Jab tak current temperature stack ke top wale temperature se bada hai
            while stack and t[stack[-1]] < temp:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            
            stack.append(i)

        return ans