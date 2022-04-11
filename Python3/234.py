# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution0:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        nodeVals = []
        while temp:
            nodeVals.append(temp.val)
            temp = temp.next
            
        length = len(nodeVals)
        
        if length%2 == 0:
            if nodeVals[0:length//2] == nodeVals[length//2:][::-1]:
                return True
        
        else:
            if nodeVals[0:length//2] == nodeVals[length//2+1:][::-1]:
                return True
            
        return False

class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        nodeVals = []
        while temp:
            nodeVals.append(temp.val)
            temp = temp.next
            
        for i in range(0, len(nodeVals)//2):
            if nodeVals[i] != nodeVals[-1-i]: return False
            
        return True

class Solution2: #implements slow and fast pointer, but is actually slower than previous solutions
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
            
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
            
        return True

class Solution3: #simpler version of solution0
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        nodeVals = []
        while temp:
            nodeVals.append(temp.val)
            temp = temp.next
            
        return nodeVals == nodeVals[::-1]