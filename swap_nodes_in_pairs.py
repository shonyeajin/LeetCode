# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left = head
        while left and left.next:
            right = left.next
            temp = left.val
            left.val = right.val
            right.val = temp
            left = right.next
        return head
