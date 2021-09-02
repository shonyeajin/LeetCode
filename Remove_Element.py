class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]==val:
                del nums[i]
            else:
                i+=1
        return len(nums)


a=[0,1,2,2,3,0,4,2]
c=Solution()
print("return value:{} and array:{}".format(c.removeElement(a,2),a))