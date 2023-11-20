# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPoint = head
        fastPoint = head
        while fastPoint and fastPoint.next:
            slowPoint = slowPoint.next
            fastPoint = fastPoint.next.next
            if slowPoint == fastPoint:
                return True
        
        return False