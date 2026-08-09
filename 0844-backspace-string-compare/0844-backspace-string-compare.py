class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # n=len(s)
        # m=len(t)
        # s1=[]
        # s2=[]
        # for i in s:
        #     if s1 and i=='#':
        #         s1.pop()
        #     elif i!='#':
        #         s1.append(i)
        # for i in t:
        #     if s2 and i=='#':
        #         s2.pop()
        #     elif i!="#":
        #         s2.append(i)
        # return s1==s2
        # isme tem jyada lg rha h 


        # i=0
        # while i<m or i<n:
        #     if i<n:
        #         if s1 and s[i]=='#':
        #             s1.pop()
        #         elif s[i]!="#":
        #             s1.append(s[i])
        #     if i<m:
        #         if s2 and t[i]=='#':
        #             s2.pop()
        #         elif t[i]!="#":
        #             s2.append(t[i])
        #     i+=1
        # return s1==s2


        i=len(s)-1
        j=len(t)-1
        s1=s2=0
        while i>=0 or j>=0:
            while i>=0:
                if s[i]=='#':
                    s1+=1
                    i-=1
                elif s1>0:
                    i-=1
                    s1-=1
                else:
                    break
            while j>=0:
                if t[j]=='#':
                    s2+=1
                    j-=1
                elif s2>0:
                    j-=1
                    s2-=1
                else:
                    break
            if i>=0 and j>=0:
                if s[i]!=t[j]:
                    return False
            i-=1
            j-=1
        if i!=j:
            return False
        return True