# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ret = ListNode()
        temp = ret
        while lists != []:
            val = 10000
            i = 0
            idx = 0
            while i < len(lists):
                print("debugging))i:{}, len:{}".format(i, len(lists), lists))
                if not lists[i]:
                    print("del list"+str(i))
                    del lists[i]
                    continue
                # print("debugging:{}".format(type(lists[i])))
                if val > lists[i].val:
                    val = lists[i].val
                    idx = i
                i += 1
            if val < 10000:
                temp.next = ListNode(val)
                temp = temp.next
                lists[idx] = lists[idx].next

        return ret.next


c = Solution()
# l1 = ListNode(1)
# l1.next = ListNode(4)
# l1.next.next = ListNode(5)
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)
# l3 = ListNode(2)
# l3.next = ListNode(6)

ret = c.mergeKLists([ListNode(2), [], ListNode(-1)])
while ret:
    print(ret.val)
    ret = ret.next
