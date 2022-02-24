
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        temp = head
        length = 1
        while temp.next is not None:
            length += 1
            temp = temp.next
        temp.next = head
        m = k % length
        for i in range(length-m):
            prev = head
            head = head.next
        prev.next = None
        return head


c1 = ListNode(1)
c2 = ListNode(2)
c3 = ListNode(3)
c4 = ListNode(4)
c5 = ListNode(5)
c1.next = c2
c2.next = c3
c3.next = c4
c4.next = c5
head = c1
c = Solution()
head = c.rotateRight(head, 2)
while head is not None:
    print(head.val)
    head = head.next
