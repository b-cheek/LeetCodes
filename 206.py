# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution0:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head
            
        front = head
        newFront = head.next
        while newFront:

            head.next = newFront.next #switch actual nodes
            newFront.next = front
            
            temp = head #switch names
            front = newFront
            newFront = temp
            newFront = newFront.next
            
        return front        

class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListRecursive(self, head: Optional[ListNode], newHead: Optional[ListNode]):
            if not head:
                return newHead
            nextNode = head.next
            head.next = newHead
            return reverseListRecursive(self, nextNode, head)
        
        return reverseListRecursive(self, head, None) 

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        while (head):
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode

        return newHead
