#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=1, next=None):
        self.val = val
        self.next = next
class Solution0:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):

        # This is not necessary
        if not l1:
            return l2
        if not l2:
            return l1
        
        ans = head = ListNode()

        while l1 and l2: 
            if l1.val<=l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next

        if l1: ans.next = l1
        if l2: ans.next = l2 # could just be else
        
        return head.next

class Solution1: # Recursive woo
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1<list2:
            list1.next = mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = mergeTwoLists(list1, list2.next)
            return list2
            
