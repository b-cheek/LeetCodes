# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution0:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        totalNodes = 0
        temp = head
        while temp:
            temp = temp.next
            totalNodes += 1
        
        targetNode = totalNodes // 2

        temp = head
        for i in range (0, targetNode):
            temp = temp.next
            
        return temp

class Solution1:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        res = head
        totalNodes = 0
        while temp:
            temp = temp.next
            totalNodes += 1
            if totalNodes%2 == 0:
                res = res.next
                
        return res
