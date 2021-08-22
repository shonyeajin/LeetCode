class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parent_dict = {'(': ')', '{': '}', '[': ']'}

        close_stack = []

        for char in s:

            if not close_stack:
                if char in parent_dict:
                    close_stack.append(parent_dict[char])
                else:
                    return False
            else:
                if char in parent_dict:
                    close_stack.append(parent_dict[char])
                else:
                    if char != close_stack.pop():
                        return False
        return close_stack == []


c = Solution()
print(c.isValid("{[]}"))
