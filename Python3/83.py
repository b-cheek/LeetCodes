# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        temp = node.next
        while (node.next != None):
            while (temp.next.val==node.val):
                temp = temp.next
            node.next = temp
                    
        return head

class Solution1: #recursive, cute but bad
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head

print(Soultion().deleteDuplicates(head))