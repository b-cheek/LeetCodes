# Merge Two Sorted Lists

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
            
class Solution2: # Personally prefer this iterative solution
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        cur = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        # Or use short-circuiting for above line:
        # cur.next = list1 or list2
        return dummyHead.next

class Solution3: # Personally prefer this recursive solution
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2