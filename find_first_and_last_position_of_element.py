class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_length = len(nums)
        if nums_length == 0:
            return [-1, -1]
        l = 0
        r = nums_length-1
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        if nums[l] == target:
            start, end = 0, 0
            temp = l
            while temp >= 0 and nums[temp] == target:
                start = temp
                temp -= 1
            temp = l
            while temp < nums_length and nums[temp] == target:
                end = temp
                temp += 1
            return [start, end]
        return [-1, -1]