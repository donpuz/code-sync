# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # O(n) space sol
        # # mark each node as visited? if visited before reaching null, then cycle
        # # visited set
        # visited = []
        # while head:
        #     if head in visited:
        #         return True
        #     visited.append(head)
        #     head = head.next
        
        # return False

        # O(1) space sol using tortoise hare algo
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            head = head.next

            if fast is head:
                return True
        
        return False