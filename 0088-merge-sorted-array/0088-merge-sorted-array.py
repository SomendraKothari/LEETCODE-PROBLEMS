class Solution(object):
    def merge(self, n1, m, n2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:n+m]=nums2
        # nums1.sort()

        i=m-1
        j=n-1
        l=m+n-1
        while j>=0:
            if i<0 or n2[j]>n1[i]:
                n1[l]=n2[j]
                j-=1
            else:
                n1[l]=n1[i]
                i-=1
            l-=1