class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_length = len(nums)
        if nums_length == 0:
            return 0
        l, r = 0, nums_length-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        if nums[l] < target:
            return l+1
        return l