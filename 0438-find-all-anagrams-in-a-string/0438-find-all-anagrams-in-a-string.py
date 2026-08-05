class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []
        ls=[0]*26
        lp=[0]*26
        for i in range(len(p)):
            ls[ord(s[i])-97]+=1
            lp[ord(p[i])-97]+=1
        ans=[]
        if lp==ls:
            ans.append(0)
        lep=len(p)
        for i in range(lep,len(s)):
            ls[ord(s[i])-97]+=1
            ls[ord(s[i-lep])-97]-=1
            if lp==ls:
                ans.append(i-lep+1)
        return ans