# Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=""
        num2=""
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        strSum = str(int(num1[::-1])+int(num2[::-1]))[::-1]
        if len(strSum)==1: return ListNode(int(strSum[0]))
        cur = ListNode(int(strSum[1]))
        result = ListNode(int(strSum[0]), cur)
        for i in range (2, len(strSum)):
            cur.next = ListNode(int(strSum[i]))
            cur = cur.next

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curSum = str(l1.val + l2.val)
        result = ListNode(int(curSum[-1]))
        remainder = curSum[0] if (len(curSum)>1) else 0
        cur = result
        while l1 or l2:
            print (l1, l2)
            if not l1:
                cur.next = ListNode(l2.val + remainder)
                remainder = int(curSum[0]) if (len(curSum)>1) else 0
                l2=l2.next
            elif not l2:
                cur.next = ListNode(l1.val + remainder)
                remainder = int(curSum[0]) if (len(curSum)>1) else 0
                l1=l1.next
            else:
                curSum = str(l1.next.val + l2.next.val + remainder)
                cur.next = ListNode(int(curSum[-1]))
                remainder = int(curSum[0]) if (len(curSum)>1) else 0
                cur = cur.next
                l1 = l1.next
                l2 = l2.next
        return result