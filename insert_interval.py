class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        out = []
        flag = 0
        if not intervals:
            return [newInterval]
        for i, n in enumerate(intervals):
            if newInterval[0] > n[1] or newInterval[1] < n[0]:
                out.append(n)
            else:
                if not flag:
                    out.append(newInterval)
                    flag = 1
                out[-1] = [min(n[0], out[-1][0]), max(n[1], out[-1][1])]
        if not flag:
            out.append(newInterval)
            out = sorted(out, key=lambda i: i[0])
        return out


c = Solution()
print(c.insert([[1, 5]], [6, 8]))
