class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first=0
        end=len(height)-1
        totalMax=0
        while first<end:
            totalMax=max(min(height[first],height[end])*(end-first),totalMax)
            if height[first]>height[end]:
                end-=1
            else:
                first+=1
        return totalMax
c=Solution()
print(c.maxArea([0,0]))