# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret=ListNode()
        temp=ret
        while (l1!=None and l2!=None):
            sum = temp.val + l1.val + l2.val
            temp.val = sum % 10
            temp.next = ListNode(sum / 10)
            prev = temp
            temp = temp.next
            l1=l1.next
            l2=l2.next

        while l1 != None:
            sum = l1.val + temp.val
            temp.val = sum % 10
            temp.next = ListNode(sum / 10)
            l1 = l1.next
            prev = temp
            temp = temp.next

        while l2 != None:
            sum = l2.val + temp.val
            temp.val = sum % 10
            temp.next = ListNode(sum / 10)
            l2 = l2.next
            prev = temp
            temp = temp.next       
        
        if temp.val == 0:
            prev.next = None
        
        return (ret)


            



