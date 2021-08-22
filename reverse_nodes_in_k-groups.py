# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def checkNode(self, head, k):
        while k > 0:
            if not head:
                return False
            head = head.next
            k -= 1
        return True

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        temp = head
        while self.checkNode(temp, k):
            temp2 = temp
            saveList = []
            i = k
            while i > 0:
                saveList.append(temp2.val)
                temp2 = temp2.next
                i -= 1
            i = k
            while i > 0:
                temp.val = saveList[i-1]
                temp = temp.next
                i -= 1

        return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
c = Solution()
ret = c.reverseKGroup(l, 2)

while ret:
    print(ret.val)
    ret = ret.next
