# Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution0:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        nodes = []
        while temp:
            if temp in nodes: return True
            else: nodes.append(temp)
            temp = temp.next
        return False

class Solution1: # This is the optimal solution, O(n) time, O(1) space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next.next
        return False

class Solution2: # Lol
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False