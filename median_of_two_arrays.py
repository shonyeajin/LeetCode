class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)==0 and len(nums2)==0:
            return (0)
        idx1 = idx2 = 0
        ret=[]
        i=0
        while i<=(len(nums1)+len(nums2))/2:
            if idx1<len(nums1) and idx2<len(nums2) and nums1[idx1] <= nums2[idx2]:
                ret.append(nums1[idx1])
                idx1+=1
            elif idx1<len(nums1) and idx2<len(nums2) and nums1[idx1] > nums2[idx2]:
                ret.append(nums2[idx2])
                idx2+=1
            elif idx1==len(nums1):
                ret.append(nums2[idx2])
                idx2+=1
            else:
                ret.append(nums1[idx1])
                idx1+=1
            i+=1
        if (len(nums1)+len(nums2)) % 2 == 0:
            return (ret[i-2]+ret[i-1])/2
        else:
            return ret[i-1]
c=Solution()
ret=c.findMedianSortedArrays([3,4],[1,2])
print(ret)
