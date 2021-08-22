# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        total=count=prev=0
        temp=head
        while temp != None:
            total+=1
            temp=temp.next
        temp=head
        target=total-n+1
        while count<total:
            count+=1
            if count==target:
                if prev != 0:
                    prev.next=temp.next
                    return head
                else:
                    head=temp.next
                    return head
            else:
                prev=temp
                temp=temp.next
        return head

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)

n1.next=n2
n2.next=n3

c=Solution()
print(c.removeNthFromEnd(n1,1))