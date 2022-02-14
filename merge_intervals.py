class Solution(object):
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out


c = Solution()
print(c.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
