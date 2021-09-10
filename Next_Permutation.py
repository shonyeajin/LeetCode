class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx_i=-1
        idx_j=0
        i=0
        nums_length=len(nums)
        if nums_length==0 or nums_length==1:
            return
        while i+1< nums_length:
            if nums[i]<nums[i+1]:
                idx_i=i
            i+=1
        if idx_i==-1:
            i=0
            while i<nums_length/2:
                nums[i],nums[nums_length-i-1]=nums[nums_length-i-1],nums[i]
                i+=1
            return
        i=nums_length-1
        while idx_i<i:
            if nums[idx_i]<nums[i]:
                idx_j=i
                break
            i-=1
        nums[idx_i],nums[idx_j]=nums[idx_j],nums[idx_i]
        idx_i+=1
        i=nums_length-1
        while idx_i<i:
            nums[idx_i],nums[i]=nums[i],nums[idx_i]
            idx_i+=1
            i-=1
        return 

a=[5,1,1]
c=Solution()
c.nextPermutation(a)
print(a)
#https://jins-dev.tistory.com/entry/%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-%EC%B0%BE%EA%B8%B0-%EC%A0%84%EC%B2%B4-%EC%88%9C%EC%97%B4-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Next-Permutation



