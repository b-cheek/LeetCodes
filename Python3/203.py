# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution0:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
            
        if head == None: return head
        
        slow = head
        fast = head.next
        
        while slow and fast:
            if fast.val==val:
                while fast and fast.val==val:
                    fast = fast.next
                slow.next = fast
            slow = slow.next
            if fast: fast = fast.next
            
            
        return head

class Solution1:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next

class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head
        head.next=(self.removeElements(head.next))
        return head.next if head.val==val else head
