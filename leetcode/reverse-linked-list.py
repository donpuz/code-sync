# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev: null | 1 -> 2 -> 3
        # init prev
        # below is in loop
        # keep temp for curr.next
        # set curr.next to prev
        # set prev to curr
        # set curr to temp

        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev