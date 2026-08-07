class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # s="HBFUGBKDNHIIUBIDHUSDBFISDHFIU"
        # t="II"

        # m=len(s)
        # n=len(t)
        # if m<n:
        #     return ""
        # d={}
        # ans=" "*m
        # for i in t:
        #     d[i]=d.get(i,0)+1
        # req=len(d)
        # f={}
        # c=0
        # l=0
        # g=0
        # for i in range(m):
        #     if i==0 and s[i] not in d:
        #         l+=1
        #         while l<m and s[l] not in d:
        #             l+=1
        #         continue
        #     if s[i] in d:
        #         f[s[i]]=f.get(s[i],0)+1
        #         if f[s[i]]>d[s[i]] and s[l]==s[i]:
        #             f[s[l]]-=1
        #             l+=1
        #             while l<i and s[l] not in d:
        #                 l+=1
        #         elif f[s[i]]==d[s[i]]:
        #             c+=1
        #         if c==req:
        #             g+=1
        #             if len(ans)>=(i-l+1):
        #                 ans=s[l:i+1]
        #             print(ans)
        #             f[s[l]]-=1
        #             c-=1
        #             l+=1
        #             while l<i and s[l] not in d:
        #                 l+=1
        #             print(f,i)
        #             if l<i and f[s[l]]>d[s[l]]:
        #                 e=s[l]
        #                 l+=1
        #                 f[e]-=1
        #                 while f[e]>d[e] and s[l] not in d:
        #                     l+=1
        #                     if s[l]==e:
        #                         f[e]-=1        
        # if g==0:
        #     ans=""     
        # return ans
        # glt h yeh code🤧

        m=len(s)
        n=len(t)
        if m<n:
            return ""
        d={}
        ans=float("inf"),None,None
        for i in t:
            d[i]=d.get(i,0)+1
        req=len(d)
        f={}
        c=0
        l=0
        r=0
        while r<m:
            ch=s[r]
            f[ch]=f.get(ch,0)+1
            if ch in d and f[ch]==d[ch]:
                c+=1
            while l<=r and c==req:
                if ans[0]>r-l+1:
                    ans=(r-l+1,l,r)
                g=s[l]
                f[g]-=1
                if g in d and f[g]<d[g]:
                    c-=1
                l+=1
            r+=1
        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]