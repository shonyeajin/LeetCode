class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,mid=0,0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivot=l
        if target>nums[-1]:
            l,r=0,pivot
        else:
            l,r=pivot,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        if nums[l]!=target:
            return -1
        return l
c=Solution()
print(c.search([1],0))