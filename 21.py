#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=1, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        
        # ans = ListNode()

        # if l1.val<=l2.val:
        #     ans = l1
        #     ans.next = self.mergeTwoLists(l1.next, l2)
        # else:
        #     ans = l2
        #     ans.next = self.mergeTwoLists(l1, l2.next)

        # return ans

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
        if l2: ans.next = l2
        
        return head.next