# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def dp(self, node, sum, ret):
        if node.left == None and node.right == None:
            ret.append(sum*10+node.val)
            return
        if node.left != None:
            self.dp(node.left, sum*10+node.val, ret)
        if node.right != None:
            self.dp(node.right, sum*10+node.val, ret)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []
        if root.left == None and root.right == None:
            return root.val
        if root.left != None:
            self.dp(root.left, root.val, ret)
        if root.right != None:
            self.dp(root.right, root.val, ret)
        return sum(ret)


a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# a.left = b
# a.right = c
cal = Solution()
print(cal.sumNumbers(a))
