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

print(Soultion().deleteDuplicates(head))