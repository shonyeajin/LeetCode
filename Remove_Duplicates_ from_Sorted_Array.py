class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers=set([])
        i=0
        while i<len(nums):
            if nums[i] not in numbers:
                numbers.add(nums[i])
                i+=1
            else:
                del nums[i]
        return len(nums)

c=Solution()
print(c.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))