# Reverse Linked List

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

class Solution1:    #recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Note that I find the use of newHead to be mostly confusing, see S3
        def reverseListRecursive(self, head: Optional[ListNode], newHead: Optional[ListNode]):
            if not head:
                return newHead
            nextNode = head.next
            head.next = newHead
            return reverseListRecursive(self, nextNode, head)
        
        return reverseListRecursive(self, head, None) 

class Solution2:    #iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        while (head):
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode

        return newHead

class Solution3: # Same as above, I think it's more readable though
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head is the current node, prev is the previous node, which starts as None
        prev = None
        while head:
            nextNode = head.next
            # Point the current node to whatever is behind it
            head.next = prev
            # Move prev and head forward
            prev = head
            head = nextNode

        # Once the current node is none, it's prev will be the last node of old list
        return prev