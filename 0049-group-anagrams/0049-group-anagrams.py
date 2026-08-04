class Solution(object):
    def groupAnagrams(self, s):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for i in s:
            ss="".join(sorted(i))
            if ss in d:
                d[ss].append(i)
            else:
                d[ss]=[i]
        return d.values()